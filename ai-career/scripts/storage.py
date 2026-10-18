#!/usr/bin/env python3
"""定位、原位初始化三个 AI 职业技能共用的数据目录；仅使用标准库。"""

import argparse
import importlib.util
import json
import os
from pathlib import Path
import sqlite3
import tempfile


class StorageError(ValueError):
    pass


def absolute_path(value, base=None):
    if not isinstance(value, (str, os.PathLike)) or not str(value).strip():
        raise StorageError("数据路径必须为非空路径")
    path = Path(value).expanduser()
    if base is not None and not path.is_absolute():
        path = base / path
    return path.resolve()


def read_object(path):
    if not path.exists():
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise StorageError(f"无法读取 JSON：{path}；{exc}") from exc
    if not isinstance(value, dict):
        raise StorageError(f"JSON 必须是对象：{path}")
    return value


def config_path(config=None):
    if config is not None:
        return absolute_path(config)
    directory = os.environ.get("XDG_CONFIG_HOME") or "~/.config"
    return absolute_path(Path(directory).expanduser() / "ai-career/storage.json")


def read_registry(path):
    registry = read_object(path)
    if registry is None:
        return None
    if registry.get("schema_version") != 1:
        raise StorageError(f"不支持的 storage.json schema_version：{path}")
    root = registry.get("default_root")
    if not isinstance(root, str) or not root.strip() or not Path(root).is_absolute():
        raise StorageError(f"storage.json 的 default_root 必须为绝对路径：{path}")
    return registry


def existing_workspace(workspace):
    return any((workspace / entry).exists() for entry in (
        "data/jobs.sqlite3", "data/jobs-watchlist.json", "data/radar/watchlist.json",
    ))


def describe(root, selected_by, config, registry):
    if root.exists() and not root.is_dir():
        raise StorageError(f"数据根路径不是目录：{root}")
    jobs_watchlist = root / "data/jobs-watchlist.json"
    radar_watchlist = root / "data/radar/watchlist.json"
    jobs = read_object(jobs_watchlist) or {}
    radar = read_object(radar_watchlist) or {}
    paths = {
        "jobs_db": absolute_path(jobs.get("ledger", "data/jobs.sqlite3"), root),
        "jobs_watchlist": jobs_watchlist,
        "jobs_observations": root / "data/observations",
        "radar_watchlist": radar_watchlist,
        "radar_runs": root / "data/radar/runs",
        "evidence": root / "data/evidence",
        "reports": root / "reports",
    }
    file_names = {"jobs_db", "jobs_watchlist", "radar_watchlist"}
    for name, path in paths.items():
        if path.exists() and not (path.is_file() if name in file_names else path.is_dir()):
            raise StorageError(f"数据路径类型冲突：{name} = {path}")
    baselines = {}
    for name, watchlist, field in (
        ("jobs_observations", jobs, "baseline_observations"),
        ("radar_catalog", radar, "baseline"),
        ("radar_input", radar, "baseline_input"),
        ("career_handoff", radar, "career_handoff"),
        ("jobs_report", jobs, "report"),
        ("radar_report", radar, "report"),
    ):
        value = watchlist.get(field)
        baselines[name] = None if value is None else str(absolute_path(value, root))
    return {
        "root": str(root),
        "selected_by": selected_by,
        "config": str(config),
        "initialized": all(path.exists() for path in paths.values()),
        "registered": registry is not None and absolute_path(registry["default_root"]) == root,
        "paths": {name: str(path) for name, path in paths.items()},
        "baselines": baselines,
    }


def resolve(root=None, workspace=None, config=None):
    """只读定位；当前目录之外的历史库只通过显式路径、环境变量或登记表查找。"""
    workspace = absolute_path(workspace if workspace is not None else Path.cwd())
    config = config_path(config)
    registry = read_registry(config)
    if root is not None:
        selected, selected_by = absolute_path(root), "explicit"
    elif os.environ.get("AI_CAREER_DATA_ROOT"):
        selected, selected_by = absolute_path(os.environ["AI_CAREER_DATA_ROOT"]), "environment"
    elif existing_workspace(workspace):
        selected, selected_by = workspace, "workspace"
    elif registry is not None:
        selected, selected_by = absolute_path(registry["default_root"]), "registry"
        if not selected.is_dir():
            raise StorageError(f"已登记的数据目录不存在：{selected}；请恢复目录或用 --root 明确指定其他库")
    else:
        directory = os.environ.get("XDG_DATA_HOME") or "~/.local/share"
        selected, selected_by = absolute_path(Path(directory).expanduser() / "ai-career"), "default"
    return describe(selected, selected_by, config, registry)


def write_registry(path, registry):
    """登记表原子更新；内容相同则保持原文件及其修改时间。"""
    if read_registry(path) == registry:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=".storage-", suffix=".json", delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(json.dumps(registry, ensure_ascii=False, indent=2) + "\n")
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return True


def initialize_jobs(db):
    script = Path(__file__).resolve().parents[2] / "ai-jobs/scripts/job_ledger.py"
    if not script.is_file():
        raise StorageError(f"初始化岗位库需要同级安装的 ai-jobs：{script}")
    spec = importlib.util.spec_from_file_location("ai_career_job_ledger", script)
    ledger = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ledger)
    ledger.initialize(db)


def init(root=None, workspace=None, config=None):
    """只补缺失项，原位采用已有库；不搬迁或重写已有观察及清单。"""
    result = resolve(root=root, workspace=workspace, config=config)
    selected = Path(result["root"])
    paths = {name: Path(value) for name, value in result["paths"].items()}
    created = []
    directories = [selected, paths["jobs_db"].parent, paths["jobs_watchlist"].parent,
                   paths["radar_watchlist"].parent]
    directories.extend(paths[name] for name in ("jobs_observations", "radar_runs", "evidence", "reports"))
    for directory in directories:
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
            created.append(str(directory))
    defaults = {
        "jobs_watchlist": {
            "ledger": "data/jobs.sqlite3", "sources": [], "tracked_jobs": [], "scope": {},
            "baseline_observations": None, "last_run": None, "report": None,
        },
        "radar_watchlist": {
            "sources": [], "scope": {}, "baseline": None, "baseline_input": None,
            "last_run": None, "job_context": [], "report": None,
        },
    }
    for name, contents in defaults.items():
        path = paths[name]
        if not path.exists():
            with path.open("x", encoding="utf-8") as stream:
                stream.write(json.dumps(contents, ensure_ascii=False, indent=2) + "\n")
            created.append(str(path))
    if not paths["jobs_db"].exists():
        initialize_jobs(paths["jobs_db"])
        created.append(str(paths["jobs_db"]))
    config = Path(result["config"])
    registry = {**(read_registry(config) or {}), "schema_version": 1, "default_root": str(selected)}
    new_config = not config.exists()
    write_registry(config, registry)
    if new_config:
        created.append(str(config))
    result = describe(selected, result["selected_by"], config, registry)
    result["created"] = created
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command, description in (("resolve", "只读查找数据目录和历史基线"), ("init", "补齐缺失目录并登记共享库")):
        subparser = commands.add_parser(command, help=description)
        subparser.add_argument("--root", help="明确指定数据根目录")
        subparser.add_argument("--workspace", help="检查已有库的工作目录，默认当前目录")
        subparser.add_argument("--config", help="覆盖共享数据登记表路径")
    args = parser.parse_args(argv)
    try:
        operation = init if args.command == "init" else resolve
        result = operation(root=args.root, workspace=args.workspace, config=args.config)
    except (OSError, ValueError, sqlite3.Error) as exc:
        parser.exit(2, f"storage: {exc}\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
