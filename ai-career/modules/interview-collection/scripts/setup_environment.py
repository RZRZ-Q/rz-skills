#!/usr/bin/env python3
"""按本轮功能检查环境；仅 install 会向指定 runtime 安装可选依赖。"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


FEATURES = ("local", "nowcoder", "browser", "feishu", "excel", "pdf")
# 2026-10-09 从 npm / PyPI 官方版本 API 核对。新增安装固定直接依赖；已有可用工具保留。
OPENCLI_VERSION = "1.8.8"
NODE_MINIMUM = (20, 18, 1)
PYTHON_PACKAGES = {"excel": ("openpyxl", "3.1.5"), "pdf": ("pypdf", "6.19.0")}
LARK_INSTALL = "https://github.com/larksuite/cli#installation--quick-start"


def parse_features(value):
    selected = list(dict.fromkeys(part.strip() for part in value.split(",")))
    unknown = [part for part in selected if part not in FEATURES]
    if unknown:
        raise argparse.ArgumentTypeError("未知功能：" + ", ".join(unknown))
    return selected


def probe(command):
    """只运行版本或隔离的 Python 导入检查，不连接平台或读取认证。"""
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.TimeoutExpired) as error:
        return None, str(error)
    output = (result.stdout or result.stderr).strip()
    if result.returncode:
        return None, f"退出 {result.returncode}: {output[:500]}"
    return output, None


def tool_status(name, path, required=True):
    item = {"name": name, "path": str(path) if path else None, "required": required}
    if not path:
        return dict(item, status="missing", version=None)
    output, error = probe([str(path), "--version"])
    if error:
        return dict(item, status="unusable", version=None, detail=error)
    return dict(item, status="available", version=output.splitlines()[0] if output else "")


def runtime_python(runtime):
    return runtime / "python" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")


def python_package_status(feature, runtime):
    package, pinned = PYTHON_PACKAGES[feature]
    interpreters = [runtime_python(runtime)] if runtime and runtime_python(runtime).is_file() else []
    if Path(sys.executable) not in interpreters:
        interpreters.append(Path(sys.executable))
    api = "load_workbook" if feature == "excel" else "PdfReader"
    code = (
        "import importlib.util, sys; "
        f"sys.exit(3) if importlib.util.find_spec({package!r}) is None else None; "
        f"from {package} import {api}; "
        f"from importlib.metadata import version; print(version({package!r}))"
    )
    errors = []
    for interpreter in interpreters:
        version, error = probe([str(interpreter), "-I", "-B", "-c", code])
        if not error:
            return {"name": package, "status": "available", "version": version,
                    "path": str(interpreter), "required": True, "install_version": pinned}
        errors.append(f"{interpreter}: {error}")
    return {"name": package, "status": "missing", "version": None, "path": None,
            "required": True, "install_version": pinned, "detail": errors}


def check(features, runtime):
    tools = [{"name": "python", "status": "available" if sys.version_info >= (3, 9) else "unusable",
              "version": sys.version.split()[0], "path": sys.executable, "required": True}]
    pending = ["Agent 宿主、模型额度与文件能力由宿主提供；此脚本不能验证。涉及图片时另需读图能力。"]
    steps = []
    if "browser" in features:
        local = runtime / "npm" / "node_modules" / ".bin" / ("opencli.cmd" if os.name == "nt" else "opencli") if runtime else None
        opencli = tool_status("opencli", local if local and local.is_file() else shutil.which("opencli"))
        node = tool_status("node", shutil.which("node"))
        if node["status"] == "available":
            match = re.search(r"(\d+)\.(\d+)\.(\d+)", node["version"])
            if not match or tuple(map(int, match.groups())) < NODE_MINIMUM:
                node.update(status="unusable", detail="公开安装版本需要 Node.js >=20.18.1。")
        tools.extend([opencli, node, tool_status("npm", shutil.which("npm"), required=False)])
        pending.append("Chrome/Chromium、Browser Bridge、指定 profile 的连接与平台登录尚未检查；不自动启动浏览器。")
        pending.append("OpenCLI 这里只验证可执行版本；--profile、browser <session>、--window background 等本轮参数仍需按平台说明核对。")
        steps.append("缺少 Node.js/npm 时按 https://nodejs.org/en/download 安装；之后重新检查。")
        if opencli["status"] != "available":
            steps.append("选择 browser 并指定 runtime 后运行 install，可局部安装公开固定版 OpenCLI。")
        steps.append("按 https://github.com/jackwener/OpenCLI#quick-start 在所选 Chrome profile 启用 Bridge；用户手动登录。实际读取另按平台预算执行。")
    if "feishu" in features:
        lark = tool_status("lark-cli", shutil.which("lark-cli"))
        tools.append(lark)
        if lark["status"] != "available":
            steps.append(f"按 {LARK_INSTALL} 手动运行 npx @larksuite/cli@latest install；需 Node.js/npm，缺失时先按 Node.js 官方步骤安装。该交互流程可配置宿主，本工具不自动运行。")
        pending.append("在 Agent 宿主确认 lark-base、lark-shared 可用；用户认证、身份、目标表权限尚未检查，版本可执行不代表飞书可读写。")
    for feature in features:
        if feature in PYTHON_PACKAGES:
            item = python_package_status(feature, runtime)
            tools.append(item)
            if item["status"] != "available":
                steps.append(f"缺少 {item['name']}；只有宿主不能直接读取该格式时，才选择 {feature} 并指定 runtime 运行 install。")
    if "pdf" in features:
        pending.append("pypdf 用于可提取文本的 PDF；扫描页、公式与图像需宿主读图或另行确定 OCR，安装不等于内容已正确导入。")
    if sys.version_info < (3, 9):
        steps.append("按 https://www.python.org/downloads/ 安装 Python 3.9+ 后重试。")
    missing = [item["name"] for item in tools if item["required"] and item["status"] != "available"]
    return {"action": "check", "features": features, "runtime": str(runtime) if runtime else None,
            "tools_ready": not missing, "missing": missing, "tools": tools,
            "pending": pending, "next_steps": steps,
            "scope": "本机版本/导入检查；未搜索平台、未读取认证、未验证登录或完整业务流程。"}


def install(features, runtime):
    before = check(features, runtime)
    by_name = {item["name"]: item for item in before["tools"]}
    commands = []
    if "browser" in features and by_name["opencli"]["status"] != "available":
        if by_name["node"]["status"] != "available" or by_name["npm"]["status"] != "available":
            raise RuntimeError("安装 OpenCLI 前需可用 Node.js >=20.18.1 与 npm；请按检查报告补齐。")
        commands.append([
            by_name["npm"]["path"], "install", "--prefix", str(runtime / "npm"),
            "--cache", str(runtime / "npm-cache"), "--global=false", "--ignore-scripts",
            "--no-audit", "--no-fund", "--save-exact", f"@jackwener/opencli@{OPENCLI_VERSION}",
        ])
    packages = [f"{name}=={version}" for feature, (name, version) in PYTHON_PACKAGES.items()
                if feature in features and by_name[name]["status"] != "available"]
    if packages:
        python = runtime_python(runtime)
        if not python.is_file():
            if (runtime / "python").exists():
                raise RuntimeError("runtime/python 已存在但没有可用解释器；请选择新的 runtime，保留原目录排查。")
            commands.append([sys.executable, "-m", "venv", str(runtime / "python")])
        commands.append([str(python), "-m", "pip", "--isolated", "--disable-pip-version-check",
                         "install", "--no-cache-dir", *packages])
    # lark-cli 的官方安装会进入交互配置，明确留给用户，不把待完成写成已安装。
    if commands:
        runtime.mkdir(parents=True, exist_ok=True)
    for command in commands:
        print("安装：" + json.dumps(command, ensure_ascii=False), file=sys.stderr)
        subprocess.run(command, check=True, stdout=sys.stderr)
    result = check(features, runtime)
    result.update(action="install", installed_commands=commands)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", nargs="?", choices=("check", "install"), default="check")
    parser.add_argument("--features", type=parse_features, help="local,nowcoder,browser,feishu,excel,pdf；默认 local")
    parser.add_argument("--runtime", type=Path, help="可选依赖目录；install 必须显式指定")
    args = parser.parse_args(argv)
    if args.action == "install" and (args.runtime is None or args.features is None):
        parser.error("install 必须显式指定 --features 和 --runtime")
    features = args.features or ["local"]
    runtime = args.runtime.expanduser().resolve() if args.runtime else None
    try:
        result = install(features, runtime) if args.action == "install" else check(features, runtime)
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(json.dumps({"action": args.action, "error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["tools_ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
