#!/usr/bin/env python3
"""从一份维护源构建 ai-career 总包及可独立安装的内含模块。"""

import argparse
import os
from pathlib import Path
import re
import shutil
from urllib.parse import unquote


PROJECT = Path(__file__).resolve().parents[1]
SOURCE = PROJECT / "skills/ai-career"
if not SOURCE.is_dir():
    SOURCE = PROJECT / "ai-career"
LINK = re.compile(r"\]\(([^)]+)\)")


def files(directory):
    return [path for path in directory.rglob("*") if path.is_file()
            and "__pycache__" not in path.parts and "_shared" not in path.parts
            and path.suffix != ".pyc"
            and path.name != ".DS_Store"]


def target_of(document, href):
    if href.startswith(("#", "mailto:")) or "://" in href:
        return None
    target = (document.parent / unquote(href.split("#", 1)[0])).resolve()
    # 已生成的独立包引用回到维护源，允许从已分发仓库再次构建同样的包。
    if target.is_relative_to(SOURCE):
        relative = target.relative_to(SOURCE)
        if len(relative.parts) > 3 and relative.parts[0] == "modules" and relative.parts[2] == "_shared":
            target = SOURCE.joinpath(*relative.parts[3:])
        if target in {SOURCE / "modules" / name / "scripts/storage.py"
                      for name in ("ai-jobs", "ai-tech-radar")}:
            target = SOURCE / "scripts/storage.py"
        if target == SOURCE / "modules/ai-tech-radar/scripts/job_ledger.py":
            target = SOURCE / "modules/ai-jobs/scripts/job_ledger.py"
    if not target.is_relative_to(SOURCE) or not target.is_file():
        raise ValueError(f"无效的包内引用：{document}: {href}")
    return target


def bundle_module(name, destination):
    module = SOURCE / "modules" / name
    output = destination / "modules" / name
    generated = {module / "scripts/storage.py"}
    if name == "ai-tech-radar":
        generated.add(module / "scripts/job_ledger.py")
    mapping = {path: output / path.relative_to(module) for path in files(module) if path not in generated}
    if name in ("ai-jobs", "ai-tech-radar"):
        mapping[SOURCE / "scripts/storage.py"] = output / "scripts/storage.py"
        ledger = SOURCE / "modules/ai-jobs/scripts/job_ledger.py"
        mapping[ledger] = output / "scripts/job_ledger.py"

    # 只带被实际引用的资料；不复制另一技能的入口或启动其他工作流。
    pending = list(mapping)
    while pending:
        document = pending.pop()
        if document.suffix != ".md":
            continue
        for href in LINK.findall(document.read_text(encoding="utf-8")):
            target = target_of(document, href)
            if target is None or target in mapping:
                continue
            if target.name == "SKILL.md":
                raise ValueError(f"独立模块不能隐式带入其他 Skill 入口：{document}: {href}")
            mapping[target] = output / "_shared" / target.relative_to(SOURCE)
            pending.append(target)

    for source, target in mapping.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix != ".md":
            shutil.copy2(source, target)
            continue

        def rebase(match):
            href = match.group(1)
            linked = target_of(source, href)
            if linked is None:
                return match.group(0)
            _, separator, anchor = href.partition("#")
            relative = Path(os.path.relpath(mapping[linked], target.parent)).as_posix()
            return "](" + relative + (separator + anchor if separator else "") + ")"

        target.write_text(LINK.sub(rebase, source.read_text(encoding="utf-8")), encoding="utf-8")
    return len(mapping)


def build(destination):
    # 输出必须是新目录，避免覆盖正在使用的 Skill 或历史数据。
    destination.mkdir(parents=True, exist_ok=False)
    for source in files(SOURCE):
        if source.relative_to(SOURCE).parts[0] == "modules":
            continue
        target = destination / source.relative_to(SOURCE)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    counts = {name: bundle_module(name, destination)
              for name in ("ai-jobs", "ai-tech-radar", "interview-collection")}
    print(f"总包：{destination}")
    for name, count in counts.items():
        print(f"独立模块：modules/{name}，{count} 个文件")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path, help="尚不存在的 ai-career 输出目录")
    build(parser.parse_args().output.resolve())
