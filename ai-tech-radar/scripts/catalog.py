#!/usr/bin/env python3
"""汇总雷达材料观察，按独立工作聚合并保存不可覆盖的目录快照。"""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
from urllib.parse import urlsplit, urlunsplit


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
    parser.add_argument("--input", nargs="+", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--previous", type=Path)
    args = parser.parse_args(argv)
    try:
        snapshot = build_catalog(args.input, args.previous)
        write_catalog(snapshot, args.output)
    except (CatalogError, OSError, ValueError) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 1
    print(json.dumps(snapshot["counts"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
