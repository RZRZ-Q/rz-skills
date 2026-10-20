#!/usr/bin/env python3
"""有界读取牛客搜索片段、讨论帖与动态帖正文；只使用标准库。"""
from __future__ import annotations

import argparse
import http.client
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ENDPOINT = "https://gw-c.nowcoder.com/api/sparta/pc/search"
MAX_BYTES = 6 * 1024 * 1024
MAX_TEXT = 20_000


class TextParser(HTMLParser):
    """转换接口正文 HTML，保留分段并标记未读取的图片。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = []
        self.has_images = False

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "template", "noscript"}:
            self.hidden.append(tag)
        if self.hidden:
            return
        if tag == "img":
            self.has_images = True
        if tag in {"br", "p", "div", "li", "section", "h1", "h2", "h3", "pre"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.hidden:
            del self.hidden[self.hidden.index(tag):]
        elif not self.hidden and tag in {"p", "div", "li", "section", "h1", "h2", "h3", "pre"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)

    @property
    def text(self):
        lines = [re.sub(r"[\t \xa0]+", " ", line).strip() for line in "".join(self.parts).splitlines()]
        return "\n".join(line for line in lines if line)


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def request(url, payload=None):
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode() if payload is not None else None,
        headers={"Content-Type": "application/json", "Accept": "application/json",
                 "User-Agent": "find-interviews/1.0 (read-only; no-cookie)"},
    )
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    try:
        with opener.open(request, timeout=20) as response:
            if response.headers.get_content_type() != "application/json":
                raise ValueError("响应不是 JSON，停止访问")
            raw = response.read(MAX_BYTES + 1)
    except urllib.error.HTTPError as error:
        raise ValueError(f"HTTP {error.code}，停止访问") from None
    except (urllib.error.URLError, TimeoutError, OSError, http.client.HTTPException):
        raise ValueError("网络请求失败，停止访问") from None
    if len(raw) > MAX_BYTES:
        raise ValueError("响应超过 6 MiB，停止访问")
    return raw


def request_json(url, payload=None):
    raw = request(url, payload)
    try:
        value = json.loads(raw)
    except (ValueError, UnicodeDecodeError):
        raise ValueError("响应不是有效 JSON，停止访问") from None
    return value


def request_page(query, page):
    return request_json(ENDPOINT, {"type": "post", "query": query, "page": page, "order": "create"})


def parse_page(value, page):
    if not isinstance(value, dict) or value.get("success") is not True or type(value.get("code")) is not int or value["code"] != 0:
        raise ValueError("平台未返回成功响应，停止访问")
    data = value.get("data")
    if (not isinstance(data, dict) or type(data.get("current")) is not int or data["current"] != page
            or type(data.get("totalPage")) is not int or data["totalPage"] < 0
            or not isinstance(data.get("records"), list) or len(data["records"]) > 20):
        raise ValueError("搜索页结构不符合预期，停止访问")
    results = []
    for record in data["records"]:
        if not isinstance(record, dict) or type(record.get("contentType")) is not int:
            raise ValueError("帖子类型无效，停止访问")
        kind = record["contentType"]
        if kind not in {74, 250}:
            continue
        content = record.get("momentData" if kind == 74 else "contentData")
        if not isinstance(content, dict):
            raise ValueError("帖子内容结构无效，停止访问")
        identity = content.get("uuid" if kind == 74 else "id")
        pattern = r"[0-9a-fA-F]{32}" if kind == 74 else r"[0-9]+"
        if not isinstance(identity, str) or re.fullmatch(pattern, identity) is None:
            raise ValueError("帖子 ID 无效，停止访问")
        title, source = content.get("title"), content.get("content")
        if not isinstance(title, (str, type(None))) or not isinstance(source, (str, type(None))):
            raise ValueError("帖子文本无效，停止访问")
        parser, title_parser = TextParser(), TextParser()
        parser.feed(source or "")
        title_parser.feed(title or "")
        body = parser.text
        path = f"feed/main/detail/{identity.lower()}" if kind == 74 else f"discuss/{identity}"
        results.append({"url": f"https://www.nowcoder.com/{path}", "title": title_parser.text,
                        "text_scope": "search_excerpt",
                        "body": body[:MAX_TEXT], "body_truncated": len(body) > MAX_TEXT,
                        "has_images": parser.has_images})
    return results, not data["records"] or page >= data["totalPage"]


def search(query, pages):
    output = {"query": query, "fetched_at": datetime.now(timezone.utc).isoformat(),
              "pages_read": 0, "stop_reason": "page_limit", "results": [], "error": None}
    seen = set()
    for page in range(1, pages + 1):
        try:
            records, exhausted = parse_page(request_page(query, page), page)
        except ValueError as error:
            output.update(stop_reason="error", error=str(error))
            break
        output["pages_read"] += 1
        for record in records:
            if record["url"] not in seen:
                seen.add(record["url"])
                output["results"].append(record)
        if exhausted:
            output["stop_reason"] = "search_exhausted"
            break
    return output


def read_post(url):
    output = {"url": url, "fetched_at": datetime.now(timezone.utc).isoformat(),
              "results": [], "error": None}
    try:
        is_moment = "/feed/main/detail/" in url
        identity = url.rsplit("/", 1)[1]
        kind = "moment-data" if is_moment else "content-data"
        value = request_json(f"https://gw-c.nowcoder.com/api/sparta/detail/{kind}/detail/{identity}")
        if not isinstance(value, dict) or value.get("success") is not True:
            raise ValueError("平台未返回成功响应，停止访问")
        data = value.get("data")
        if not isinstance(data, dict) or not isinstance(data.get("content"), str):
            raise ValueError("帖子正文结构不符合预期，停止访问")
        if is_moment and (value.get("code") != 0 or data.get("uuid") != identity):
            raise ValueError("动态帖响应状态或帖子身份不符，停止访问")
        title = data.get("title")
        if not isinstance(title, (str, type(None))):
            raise ValueError("帖子标题无效，停止访问")
        body_parser, title_parser = TextParser(), TextParser()
        body_parser.feed(data["content"])
        title_parser.feed(title or "")
        body = body_parser.text
        images = data.get("imgMoment")
        if images is None:
            images = []
        if not isinstance(images, list):
            raise ValueError("图片附件结构不符合预期，停止访问")
        for field in ("createdAt", "editTime"):
            if data.get(field) is not None and type(data[field]) is not int:
                raise ValueError("帖子时间结构不符合预期，停止访问")
        output["results"].append({"url": url, "title": title_parser.text,
                                  "text_scope": "post_body", "body": body,
                                  "body_truncated": False,
                                  "created_at": data.get("createdAt"),
                                  "edited_at": data.get("editTime"),
                                  "image_attachments": images,
                                  "has_images": body_parser.has_images or bool(images)})
    except ValueError as error:
        output["error"] = str(error)
    return output


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--query")
    mode.add_argument("--url", help="规范牛客讨论帖或动态帖公开链接")
    parser.add_argument("--pages", type=int, choices=(1, 2, 3), default=1)
    parser.add_argument("--output-dir", type=Path, required=True, help="尚不存在的本地目录")
    args = parser.parse_args(argv)
    query = args.query.strip() if args.query is not None else None
    if query is not None and not 1 <= len(query) <= 200:
        parser.error("query 必须为 1–200 字符")
    if args.url is not None and (re.fullmatch(r"https://www\.nowcoder\.com/(?:discuss/[0-9]+|feed/main/detail/[0-9a-f]{32})", args.url) is None or args.pages != 1):
        parser.error("正文只接受规范牛客讨论帖或动态帖链接，且不能指定多页")
    try:
        args.output_dir.mkdir(mode=0o700)
        descriptor = os.open(args.output_dir / "results.json", os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            output = read_post(args.url) if args.url is not None else search(query, args.pages)
            json.dump(output, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
    except OSError:
        print("输出目录必须尚不存在、父目录可写；本地写入失败", file=sys.stderr)
        return 2
    print(json.dumps({"count": len(output["results"]), "pages_read": output.get("pages_read", 0),
                      "stop_reason": output.get("stop_reason", "error" if output["error"] else "post_read"),
                      "error": output["error"]}, ensure_ascii=False))
    return 1 if output["error"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
