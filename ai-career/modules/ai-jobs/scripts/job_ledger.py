#!/usr/bin/env python3
"""以不可变观察记录保存和比较 JD；仅使用 Python 标准库。"""

import argparse
import json
from pathlib import Path
import re
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from urllib.parse import urlsplit


COMPARE_FIELDS = (
    "title", "locations", "recruitment_type", "hiring_cycle", "role_family",
    "requirements", "salary", "status", "education_raw", "experience_raw",
    "candidate_stage_raw", "application_deadline",
)
DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}\Z")
DATETIME_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2}(?:\.\d{1,6})?)?(?:Z|[+-]\d{2}:\d{2})\Z")


class LedgerError(ValueError):
    pass


def initialize(db):
    """建立可直接查询的空账本；已存在时沿用原表和全部观察。"""
    db = Path(db)
    db.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db) as connection:
        connection.execute("CREATE TABLE IF NOT EXISTS observations (job_key TEXT NOT NULL, observed_at TEXT NOT NULL, payload TEXT NOT NULL, PRIMARY KEY (job_key, observed_at))")


def parse_time(value):
    if not isinstance(value, str):
        raise LedgerError("观察时间必须是带时区的 ISO8601 或 YYYY-MM-DD")
    try:
        if DATE_PATTERN.fullmatch(value):
            return datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        if DATETIME_PATTERN.fullmatch(value):
            return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except (ValueError, OverflowError) as exc:
        raise LedgerError(f"无效时间：{value}") from exc
    raise LedgerError(f"时间必须是带时区的 ISO8601 或 YYYY-MM-DD：{value}")


def utc_string(value):
    return value.isoformat(timespec="microseconds").replace("+00:00", "Z")


def cutoff(value):
    """日期的截止范围包含该 UTC 日全天；时间戳包含该时刻。"""
    parsed = parse_time(value)
    if DATE_PATTERN.fullmatch(value):
        try:
            return utc_string(parsed + timedelta(days=1)), "<"
        except OverflowError as exc:
            raise LedgerError(f"截止日期超出支持范围：{value}") from exc
    return utc_string(parsed), "<="


def require_text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise LedgerError(f"{field} 必须是非空字符串")


def require_strings(value, field):
    if not isinstance(value, list):
        raise LedgerError(f"{field} 必须是字符串数组")
    for entry in value:
        require_text(entry, field)


def validate(record):
    if not isinstance(record, dict):
        raise LedgerError("每行必须是 JSON 对象")
    for field in ("job_key", "company", "title", "source_url"):
        require_text(record.get(field), field)
    for field, choices in (
        ("recruitment_type", ("internship", "campus", "experienced", "unknown")),
        ("source_kind", ("official", "third_party", "user_document")),
        ("verification", ("live", "historical")),
        ("status", ("open", "closed", "unknown")),
    ):
        if record.get(field) not in choices:
            raise LedgerError(f"{field} 必须属于 {', '.join(choices)}")
    try:
        url = urlsplit(record["source_url"])
        if url.scheme not in ("http", "https") or not url.hostname or any(c.isspace() for c in record["source_url"]):
            raise LedgerError("source_url 必须是有效的 HTTP(S) URL")
    except ValueError as exc:
        raise LedgerError("source_url 必须是有效的 HTTP(S) URL") from exc
    observed_at = utc_string(parse_time(record.get("observed_at")))
    if record["verification"] == "historical" and record["status"] != "unknown":
        raise LedgerError("historical 观察的 status 必须为 unknown")
    if record["status"] in ("open", "closed"):
        require_text(record.get("status_evidence"), "status_evidence")
    if not isinstance(record.get("requirements"), list):
        raise LedgerError("requirements 必须是数组")
    for index, requirement in enumerate(record["requirements"]):
        prefix = f"requirements[{index}]"
        if not isinstance(requirement, dict):
            raise LedgerError(f"{prefix} 必须是对象")
        require_text(requirement.get("text"), f"{prefix}.text")
        if requirement.get("kind") not in ("must", "preferred", "responsibility", "unspecified"):
            raise LedgerError(f"{prefix}.kind 必须为 must/preferred/responsibility/unspecified")
        require_strings(requirement.get("skill_tags"), f"{prefix}.skill_tags")
    if "locations" in record:
        require_strings(record["locations"], "locations")
    if "company_tier" in record and record["company_tier"] not in ("large", "mid", "small", "unknown"):
        raise LedgerError("company_tier 必须为 large/mid/small/unknown")
    return {**record, "observed_at": observed_at}


def reject_constant(value):
    raise LedgerError(f"JSON 不允许非有限数字：{value}")


def load_input(path):
    records = []
    with Path(path).open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, 1):
            if not line.strip():
                continue
            try:
                record = validate(json.loads(line, parse_constant=reject_constant))
                payload = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
            except (LedgerError, json.JSONDecodeError, ValueError) as exc:
                raise LedgerError(f"第 {line_number} 行：{exc}") from exc
            records.append((record["job_key"], record["observed_at"], payload))
    return records


def ingest(db, input_path):
    # 整个输入先校验，事务中的任何内容冲突都会回滚本批全部新增记录。
    records = load_input(input_path)
    db = Path(db)
    db.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(db)
    inserted = 0
    duplicates = 0
    try:
        with connection:
            connection.execute("CREATE TABLE IF NOT EXISTS observations (job_key TEXT NOT NULL, observed_at TEXT NOT NULL, payload TEXT NOT NULL, PRIMARY KEY (job_key, observed_at))")
            for job_key, observed_at, payload in records:
                existing = connection.execute(
                    "SELECT payload FROM observations WHERE job_key = ? AND observed_at = ?",
                    (job_key, observed_at),
                ).fetchone()
                if existing:
                    if existing[0] != payload:
                        raise LedgerError(f"观察冲突：{job_key} @ {observed_at}；本批未写入，原观察记录保留")
                    duplicates += 1
                else:
                    connection.execute("INSERT INTO observations VALUES (?, ?, ?)", (job_key, observed_at, payload))
                    inserted += 1
    finally:
        connection.close()
    return {"inserted": inserted, "duplicates": duplicates}


def latest(db, as_of=None):
    db = Path(db).resolve()
    parameters = ()
    predicate = ""
    if as_of is not None:
        boundary, operator = cutoff(as_of)
        predicate = f"WHERE observed_at {operator} ?"
        parameters = (boundary,)
    # 只读连接避免 list/diff 在路径写错时创建空账本。
    connection = sqlite3.connect(f"{db.as_uri()}?mode=ro", uri=True)
    try:
        rows = connection.execute(
            f"SELECT o.payload FROM observations o JOIN "
            f"(SELECT job_key, MAX(observed_at) AS observed_at FROM observations {predicate} GROUP BY job_key) current "
            "ON o.job_key = current.job_key AND o.observed_at = current.observed_at ORDER BY o.job_key",
            parameters,
        ).fetchall()
        return [json.loads(row[0]) for row in rows]
    finally:
        connection.close()


def diff(db, before, after):
    before_cutoff = cutoff(before)
    after_cutoff = cutoff(after)
    # 同一边界下，包含该时刻的范围比不包含该时刻的范围更晚。
    if (before_cutoff[0], before_cutoff[1] == "<=") > (after_cutoff[0], after_cutoff[1] == "<="):
        raise LedgerError("before 不得晚于 after")
    previous = {record["job_key"]: record for record in latest(db, before)}
    current = {record["job_key"]: record for record in latest(db, after)}
    added = []
    changed = []
    unchanged = []
    missing = object()
    for job_key, record in current.items():
        if job_key not in previous:
            added.append(record)
            continue
        changes = {}
        for field in COMPARE_FIELDS:
            old_value = previous[job_key].get(field, missing)
            new_value = record.get(field, missing)
            if field == "requirements":
                # 行号与来源引用是证据位置；只比较要求内容，保留原始排列。
                old_value = [(item["text"], item["kind"], item["skill_tags"]) for item in old_value]
                new_value = [(item["text"], item["kind"], item["skill_tags"]) for item in new_value]
            if old_value != new_value:
                changes[field] = {"before": previous[job_key].get(field), "after": record.get(field)}
        if changes:
            changed.append({"job_key": job_key, "changes": changes})
        else:
            unchanged.append({"job_key": job_key})
    return {
        "before": before,
        "after": after,
        "counts": {"added_to_sample": len(added), "changed": len(changed), "unchanged": len(unchanged)},
        "added_to_sample": added,
        "changed": changed,
        "unchanged": unchanged,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    ingest_parser = commands.add_parser("ingest", help="事务导入 JSONL 观察记录")
    ingest_parser.add_argument("--db", required=True)
    ingest_parser.add_argument("--input", required=True)
    list_parser = commands.add_parser("list", help="列出截至指定日期的每岗位最新已知观察")
    list_parser.add_argument("--db", required=True)
    list_parser.add_argument("--as-of", help="YYYY-MM-DD（包含 UTC 全天）或带时区的 ISO8601")
    diff_parser = commands.add_parser("diff", help="比较两个时间点的样本；未重见岗位保留最后已知状态")
    diff_parser.add_argument("--db", required=True)
    diff_parser.add_argument("--before", required=True)
    diff_parser.add_argument("--after", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "ingest":
            result = ingest(args.db, args.input)
        elif args.command == "list":
            result = latest(args.db, args.as_of)
        else:
            result = diff(args.db, args.before, args.after)
    except (LedgerError, OSError, sqlite3.Error) as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
