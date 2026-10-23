#!/usr/bin/env python3
"""准备采集前阅读队列，或汇总已读材料并保存不可覆盖的目录快照。"""

import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
from urllib.parse import urljoin, urlsplit, urlunsplit


METADATA_FIELDS = (
    "title", "company", "team", "authors", "published_at", "source_type",
    "topics", "modes", "related_urls",
)
TRACKING_FIELDS = ("first_seen_at", "last_seen_at")


class CatalogError(ValueError):
    pass


def require_text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise CatalogError(f"{field} 必须为非空字符串")


def string_list(value, field):
    if not isinstance(value, list):
        raise CatalogError(f"{field} 必须为字符串数组")
    for entry in value:
        require_text(entry, field)


def utc_time(value, field):
    require_text(value, field)
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise CatalogError(f"{field} 必须为带时区的 ISO8601 时间") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise CatalogError(f"{field} 必须包含时区")
    return parsed.astimezone(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def canonical_url(value):
    require_text(value, "url")
    try:
        parts = urlsplit(value)
        if parts.scheme not in ("http", "https") or not parts.hostname or any(c.isspace() for c in value):
            raise ValueError("非 HTTP(S) URL")
        if parts.username is not None or parts.password is not None:
            raise ValueError("URL 不应包含登录凭据")
        hostname = parts.hostname.lower()
        host = f"[{hostname}]" if ":" in hostname else hostname
        port = parts.port
        if port is not None and (parts.scheme, port) not in (("http", 80), ("https", 443)):
            host += f":{port}"
        return urlunsplit((parts.scheme.lower(), host, parts.path or "/", parts.query, ""))
    except ValueError as exc:
        raise CatalogError(f"无效的 HTTP(S) URL：{value}") from exc


def validate(record):
    if not isinstance(record, dict):
        raise CatalogError("材料必须为 JSON 对象")
    for field in ("material_id", "work_id", "title", "source_ref", "summary"):
        require_text(record.get(field), field)
    canonical_url(record.get("url"))
    if record.get("source_type") not in ("engineering_blog", "research_blog", "paper", "repository"):
        raise CatalogError("source_type 不属于支持的材料类型")
    if record.get("content_scope") not in ("full_text", "partial", "abstract"):
        raise CatalogError("content_scope 必须为 full_text/partial/abstract")
    company = record.get("company")
    if isinstance(company, list):
        string_list(company, "company")
    else:
        require_text(company, "company")
    for field in ("team", "published_at"):
        if field not in record:
            raise CatalogError(f"缺少字段：{field}")
        if record[field] is not None:
            require_text(record[field], field)
    for field in ("authors", "topics", "modes", "related_urls"):
        string_list(record.get(field), field)
    if not record["modes"] or any(mode not in ("engineering", "research") for mode in record["modes"]):
        raise CatalogError("modes 必须包含 engineering 或 research")
    for url in record["related_urls"]:
        canonical_url(url)
    for field, fields in (
        ("evidence", ("claim", "excerpt", "locator", "kind")),
        ("job_links", ("job_key", "requirement_excerpt", "source_ref", "relationship")),
    ):
        entries = record.get(field)
        if not isinstance(entries, list):
            raise CatalogError(f"{field} 必须为对象数组")
        for entry in entries:
            if not isinstance(entry, dict):
                raise CatalogError(f"{field} 条目必须为对象")
            for key in fields:
                require_text(entry.get(key), f"{field}.{key}")
            if field == "evidence" and entry["kind"] not in ("method", "reported_result", "constraint", "limitation"):
                raise CatalogError("evidence.kind 不属于支持的证据类型")
    result = dict(record)
    result["retrieved_at"] = utc_time(record.get("retrieved_at"), "retrieved_at")
    return result


def build_catalog(input_paths, previous_path=None):
    previous = {}
    if previous_path is not None:
        snapshot = json.loads(Path(previous_path).read_text(encoding="utf-8"))
        if not isinstance(snapshot, dict) or not isinstance(snapshot.get("materials"), list):
            raise CatalogError("previous 必须包含 materials 数组")
        for raw in snapshot["materials"]:
            record = validate(raw)
            material_id = record["material_id"]
            if material_id in previous:
                raise CatalogError(f"previous 中 material_id 重复：{material_id}")
            for field in TRACKING_FIELDS:
                record[field] = utc_time(record.get(field), field)
            if not record["first_seen_at"] <= record["retrieved_at"] <= record["last_seen_at"]:
                raise CatalogError(f"previous 中观察时间范围冲突：{material_id}")
            previous[material_id] = record

    observed = []
    for path in input_paths:
        with Path(path).open(encoding="utf-8") as source:
            for line_number, line in enumerate(source, 1):
                if line.strip():
                    try:
                        observed.append(validate(json.loads(line)))
                    except (ValueError, TypeError) as exc:
                        raise CatalogError(f"{path}:{line_number}: {exc}") from exc

    identities, urls, versions = {}, {}, {}
    earliest = {key: record["first_seen_at"] for key, record in previous.items()}
    latest = {key: record["last_seen_at"] for key, record in previous.items()}
    for record in list(previous.values()) + observed:
        material_id = record["material_id"]
        identity = (canonical_url(record["url"]), record["work_id"])
        if material_id in identities and identities[material_id] != identity:
            raise CatalogError(f"material_id 的 URL 或 work_id 冲突：{material_id}")
        identities[material_id] = identity
        if identity[0] in urls and urls[identity[0]] != material_id:
            raise CatalogError(f"同一规范 URL 对应不同 material_id，请先去重：{urls[identity[0]]}, {material_id}")
        urls[identity[0]] = material_id
        body = {key: value for key, value in record.items() if key not in TRACKING_FIELDS}
        version_key = (material_id, record["retrieved_at"])
        if version_key in versions and versions[version_key] != body:
            raise CatalogError(f"同一材料同一观察时间的内容冲突：{material_id}")
        versions[version_key] = body
        retrieved_at = record["retrieved_at"]
        earliest[material_id] = min(earliest.get(material_id, retrieved_at), retrieved_at)
        latest[material_id] = max(latest.get(material_id, retrieved_at), retrieved_at)

    current = {}
    for (material_id, retrieved_at), record in sorted(versions.items()):
        current[material_id] = record
    materials = [
        {**current[key], "first_seen_at": earliest[key], "last_seen_at": latest[key]}
        for key in sorted(current)
    ]
    work_members = {}
    for record in materials:
        work_members.setdefault(record["work_id"], []).append(record["material_id"])
    previous_works = {record["work_id"] for record in previous.values()}
    rechecked_ids = {
        record["material_id"] for record in observed
        if record["material_id"] in previous
        and record["retrieved_at"] > previous[record["material_id"]]["last_seen_at"]
    }
    changes = {
        "new_materials": sorted(set(current) - set(previous)),
        "new_works": sorted(set(work_members) - previous_works),
        "metadata_updated": sorted(
            key for key in set(current) & set(previous)
            if any(current[key][field] != previous[key][field] for field in METADATA_FIELDS)
        ),
        "not_rechecked": sorted(set(previous) - rechecked_ids),
    }
    return {
        "materials": materials,
        "works": [{"work_id": key, "material_ids": work_members[key]} for key in sorted(work_members)],
        "changes": changes,
        "counts": {"materials": len(materials), "works": len(work_members), **{key: len(value) for key, value in changes.items()}},
    }


def prepare_candidates(input_path, previous_path=None, limit=None):
    """用目录元数据和旧目录决定先读什么；不请求正文、不新增观察。"""
    if limit is not None and limit < 0:
        raise CatalogError("limit 必须为非负整数")
    source = json.loads(Path(input_path).read_text(encoding="utf-8"))
    if not isinstance(source, dict) or not isinstance(source.get("candidates"), list):
        raise CatalogError("候选文件必须包含 candidates 数组")
    # 沿用已有目录校验和身份契约，不把 related_urls 当成同材料的别名。
    previous = build_catalog([], previous_path)["materials"] if previous_path else []
    by_id = {record["material_id"]: record for record in previous}
    by_url = {canonical_url(record["url"]): record for record in previous}
    candidates, unresolved, duplicates, seen = [], [], [], {}
    for raw in source["candidates"]:
        if not isinstance(raw, dict):
            raise CatalogError("候选必须为 JSON 对象")
        entry = dict(raw)
        for field in ("title", "date_basis", "source_ref"):
            require_text(entry.get(field), field)
        if "url" not in entry:
            raise CatalogError("候选缺少 url；尚未解析详情链接时使用 null")
        if entry["url"] is not None:
            entry["url"] = canonical_url(entry["url"])
        if "published_at" not in entry:
            raise CatalogError("候选缺少 published_at；未知日期使用 null")
        published = entry["published_at"]
        date_key = ""
        if published is not None:
            require_text(published, "published_at")
            try:
                date = datetime.fromisoformat(published.replace("Z", "+00:00"))
            except ValueError as exc:
                raise CatalogError("候选 published_at 必须为 ISO8601 日期或时间，未知使用 null") from exc
            date_key = date.replace(tzinfo=date.tzinfo or timezone.utc).astimezone(timezone.utc).isoformat()
        for field in ("material_id", "work_id", "recheck_reason"):
            if entry.get(field) is not None:
                require_text(entry[field], field)
        if entry["url"] is None:
            entry["history_match"] = None
            entry["decision"] = "unresolved_url"
            unresolved.append(entry)
            continue
        matched_id = by_id.get(entry.get("material_id"))
        matched_url = by_url.get(entry["url"])
        if matched_id and canonical_url(matched_id["url"]) != entry["url"]:
            raise CatalogError("候选 material_id 的规范 URL 与历史材料冲突")
        if matched_id and matched_url and matched_id["material_id"] != matched_url["material_id"]:
            raise CatalogError("候选 material_id 与 URL 指向不同历史材料")
        history = matched_id or matched_url
        if history:
            for field in ("material_id", "work_id"):
                if entry.get(field) is not None and entry[field] != history[field]:
                    raise CatalogError(f"候选 {field} 与历史材料冲突")
                entry[field] = history[field]
        entry["history_match"] = history
        identity = ("material", history["material_id"]) if history else ("url", entry["url"])
        if identity in seen:
            first = seen[identity]
            if any(entry.get(field) != first.get(field) for field in ("published_at", "recheck_reason")):
                raise CatalogError("重复候选的依据不一致，请先归并同材料的日期/复查依据")
            entry["duplicate_of"] = first["url"]
            duplicates.append(entry)
            continue
        seen[identity] = entry
        candidates.append((date_key, entry))
    # Python 排序稳定：同日沿用发现顺序，未知日期排在已知日期之后。
    ordered = [entry for _, entry in sorted(candidates, key=lambda item: item[0], reverse=True)]
    read_queue, reuse, deferred, date_unknown = [], [], [], []
    for entry in ordered:
        if entry["published_at"] is None:
            date_unknown.append(entry)
        if entry["history_match"] is not None and not entry.get("recheck_reason"):
            entry["decision"] = "reuse"
            reuse.append(entry)
        elif limit is not None and len(read_queue) >= limit:
            entry["decision"] = "budget_unread"
            deferred.append(entry)
        else:
            entry["decision"] = "recheck" if entry["history_match"] is not None else "read"
            read_queue.append(entry)
    return {
        "candidate_input": str(Path(input_path).resolve()),
        "previous_baseline": str(Path(previous_path).resolve()) if previous_path else None,
        "limit": limit,
        "read_queue": read_queue,
        "reuse": reuse,
        "date_unknown": date_unknown,
        "deferred": deferred,
        "duplicates": duplicates,
        "unresolved": unresolved,
        "counts": {"candidates": len(ordered) + len(unresolved), "read_queue": len(read_queue), "reuse": len(reuse),
                   "date_unknown": len(date_unknown), "deferred": len(deferred), "duplicates": len(duplicates),
                   "unresolved": len(unresolved)},
    }


class DirectoryLinks(HTMLParser):
    """只解析已保存 HTML 的链接文本与 href，不请求链接目标。"""

    def __init__(self, source_url, source_ref):
        super().__init__()
        self.source_url = source_url
        self.base_url = source_url
        self.base_seen = False
        self.source_ref = source_ref
        self.current = None
        self.links = []
        self.seen = set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "base" and values.get("href") and not self.base_seen:
            self.base_url = canonical_url(urljoin(self.source_url, values["href"].strip()))
            self.base_seen = True
        if tag != "a":
            return
        href = values.get("href")
        self.current = None
        if not href or not href.strip() or href.strip().startswith("#"):
            return
        url = urljoin(self.base_url, href.strip())
        if urlsplit(url).scheme not in ("http", "https"):
            return
        self.current = {"url": canonical_url(url), "text": [], "line": self.getpos()[0]}

    def handle_data(self, data):
        if self.current is not None:
            self.current["text"].append(data)

    def handle_endtag(self, tag):
        if tag != "a" or self.current is None:
            return
        current, self.current = self.current, None
        title = " ".join("".join(current["text"]).split())
        key = (current["url"], title)
        if title and key not in self.seen:
            self.seen.add(key)
            self.links.append({"title": title, "url": current["url"],
                               "source_ref": self.source_ref, "locator": f"HTML line {current['line']}"})


def extract_directory_links(input_path, base_url):
    source_url = canonical_url(base_url)
    source_ref = str(Path(input_path).resolve())
    parser = DirectoryLinks(source_url, source_ref)
    parser.feed(Path(input_path).read_text(encoding="utf-8"))
    parser.close()
    return {"source_url": source_url, "source_ref": source_ref, "links": parser.links,
            "counts": {"links": len(parser.links)}}


def write_catalog(snapshot, output_path):
    output = Path(output_path)
    content = json.dumps(snapshot, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with output.open("x", encoding="utf-8") as destination:
            destination.write(content)
    except FileExistsError:
        if json.loads(output.read_text(encoding="utf-8")) != snapshot:
            raise CatalogError(f"输出已存在且内容不同，拒绝覆盖：{output}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--input", nargs="+", type=Path, help="已读材料 JSONL")
    inputs.add_argument("--candidates", type=Path, help="采集前候选 JSON；不读取正文")
    inputs.add_argument("--links", type=Path, help="从已保存的目录 HTML 提取实际 href；不联网")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--previous", type=Path)
    parser.add_argument("--limit", type=int, help="候选模式本轮最多读取的材料数；复用不占名额")
    parser.add_argument("--base-url", help="--links 所读目录的实际 URL，用于解析相对 href")
    args = parser.parse_args(argv)
    if args.limit is not None and args.candidates is None:
        parser.error("--limit 仅用于 --candidates")
    if bool(args.links) != bool(args.base_url):
        parser.error("--links 与 --base-url 必须一起使用")
    if args.links is not None and args.previous is not None:
        parser.error("--links 只解析目录链接，历史匹配使用 --candidates --previous")
    try:
        if args.links is not None:
            snapshot = extract_directory_links(args.links, args.base_url)
        elif args.candidates is not None:
            snapshot = prepare_candidates(args.candidates, args.previous, args.limit)
        else:
            snapshot = build_catalog(args.input, args.previous)
        write_catalog(snapshot, args.output)
    except (CatalogError, OSError, ValueError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 1
    result = snapshot["counts"]
    if args.candidates is not None:
        result = {"output": str(args.output.resolve()), "counts": snapshot["counts"],
                  "read_queue": [entry["url"] for entry in snapshot["read_queue"]],
                  "reuse": [entry["material_id"] for entry in snapshot["reuse"]],
                  "date_unknown": [entry["url"] for entry in snapshot["date_unknown"]],
                  "unresolved": [entry["title"] for entry in snapshot["unresolved"]]}
    elif args.links is not None:
        result = {"output": str(args.output.resolve()), **snapshot}
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
