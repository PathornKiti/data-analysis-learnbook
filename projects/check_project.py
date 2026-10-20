"""Project doctor: check that a project folder meets the capstone requirements.

    python projects/check_project.py path/to/your/project
    python projects/check_project.py path/to/your/project --skip-run        # don't execute run_analysis.py
    python projects/check_project.py path/to/your/project --run-notebooks   # also execute the notebooks

It prints ✅ (ok), ⚠️ (worth fixing) and ❌ (must fix). Exit code 1 if anything is ❌.
It works on a temporary COPY of your project, so running it never changes your files.
"""
import argparse
import ast
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PASS, WARN, FAIL = "✅", "⚠️ ", "❌"
IGNORE = shutil.ignore_patterns(".git", ".venv", "venv", "__pycache__", ".pytest_cache", "*.egg-info", ".ipynb_checkpoints", "node_modules")
REQUIRED_README_TOPICS = {
    "question": ("question",),
    "data": ("data",),
    "how to run": ("how to run", "usage", "getting started", "run it", "run the"),
    "findings": ("finding", "result", "summary"),
    "limitations": ("limitation",),
}
ABSOLUTE_PATH = re.compile(r"(/home/\w+|/Users/\w+|[A-Za-z]:\\\\?Users|/content/|/root/)")


def run(cmd, cwd, env=None, timeout=900):
    return subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, timeout=timeout)


def check_readme(root):
    readme = root / "README.md"
    if not readme.exists():
        return [(FAIL, "README.md", "missing")]
    text = readme.read_text(encoding="utf-8")
    headings = " | ".join(line.lstrip("#").strip().lower() for line in text.splitlines() if line.startswith("#"))
    body = text.lower()
    missing = [topic for topic, keys in REQUIRED_README_TOPICS.items() if not any(k in headings or (topic == "question" and k in body[:600]) for k in keys)]
    results = []
    results.append((FAIL, "README sections", "missing: " + ", ".join(missing)) if missing else (PASS, "README sections", "question, data, how to run, findings, limitations"))
    if re.search(r"<[A-Za-z][^>\n]{6,}>", text):
        results.append((WARN, "README placeholders", "still contains <template placeholders>; fill them in"))
    if len(text) < 800:
        results.append((WARN, "README length", "very short; explain your question, data and findings"))
    return results


def find_package(root):
    src = root / "src"
    packages = [p for p in src.iterdir() if (p / "__init__.py").exists()] if src.is_dir() else []
    return packages[0] if packages else None


def check_structure(root):
    results = []
    results.append((PASS, "dependencies listed", "") if (root / "requirements.txt").exists() or (root / "pyproject.toml").exists()
                   else (FAIL, "dependencies listed", "add requirements.txt (or pyproject.toml)"))
    results.append((PASS, ".gitignore", "") if (root / ".gitignore").exists() else (WARN, ".gitignore", "add one (ignore generated files and .venv)"))
    pkg = find_package(root)
    if pkg is None:
        results.append((FAIL, "package in src/", "expected src/<your_package>/__init__.py"))
    else:
        modules = [p for p in pkg.glob("*.py") if p.name != "__init__.py"]
        results.append((PASS, f"package src/{pkg.name}/", f"{len(modules)} modules") if len(modules) >= 3
                       else (FAIL, f"package src/{pkg.name}/", f"only {len(modules)} module(s); split logic by job (load, clean, analysis, plots, ...)"))
        total = documented = 0
        for path in modules:
            for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
                if isinstance(node, ast.FunctionDef) and not node.name.startswith("_"):
                    total += 1
                    documented += ast.get_docstring(node) is not None
        if total:
            share = documented / total
            results.append((PASS if share >= 0.8 else WARN, "docstrings", f"{documented}/{total} public functions documented"))
    results.append((PASS, "run_analysis.py", "") if (root / "run_analysis.py").exists() else (FAIL, "run_analysis.py", "missing: one command should reproduce everything"))
    raw = root / "data" / "raw"
    results.append((PASS, "raw data present", "") if raw.is_dir() and any(p for p in raw.iterdir() if p.name not in (".gitkeep", "README.md"))
                   else (WARN, "raw data present", "data/raw/ is empty; if the data can't be committed, document how to get it"))
    for doc, label in (("PROPOSAL", "proposal"), ("DATA_CARD", "data card"), ("ETHICS_CHECKLIST", "ethics checklist")):
        found = any(root.rglob(f"{doc}.md"))
        results.append((PASS, label, "") if found else (WARN, label, f"add {doc}.md (templates are in projects/templates/)"))
    return results


def check_paths(root):
    offenders = []
    for path in list(root.rglob("*.py")) + list(root.rglob("*.ipynb")):
        if any(part in (".venv", "venv", ".git", "__pycache__") for part in path.parts):
            continue
        if ABSOLUTE_PATH.search(path.read_text(encoding="utf-8", errors="ignore")):
            offenders.append(str(path.relative_to(root)))
    return [(FAIL, "no absolute paths", "found in: " + ", ".join(offenders[:5]))] if offenders else [(PASS, "no absolute paths", "")]


def check_notebook_outputs(root):
    import json
    dirty = []
    for path in root.rglob("*.ipynb"):
        if ".ipynb_checkpoints" in path.parts or ".venv" in path.parts:
            continue
        nb = json.loads(path.read_text(encoding="utf-8"))
        if any(c.get("cell_type") == "code" and (c.get("outputs") or c.get("execution_count")) for c in nb.get("cells", [])):
            dirty.append(path.name)
    return [(WARN, "notebook outputs", "stored outputs in: " + ", ".join(dirty) + " (clear them to keep diffs small)")] if dirty else [(PASS, "notebooks have no stored outputs", "")]


def check_tests_and_run(work, skip_run, run_notebooks):
    results = []
    env = dict(os.environ, PYTHONPATH=os.pathsep.join([str(work / "src"), os.environ.get("PYTHONPATH", "")]), MPLBACKEND="Agg")
    test_files = list((work / "tests").glob("test_*.py")) if (work / "tests").is_dir() else []
    if not test_files:
        results.append((FAIL, "tests", "no tests/test_*.py files"))
    else:
        n = sum(1 for f in test_files for line in f.read_text(encoding="utf-8").splitlines() if re.match(r"\s*def test_", line))
        proc = run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--no-header"], work, env)
        last = (proc.stdout.strip().splitlines() or [""])[-1]
        if proc.returncode != 0:
            results.append((FAIL, "pytest passes", last or proc.stderr[-300:]))
        else:
            results.append((PASS if n >= 3 else WARN, "pytest passes", f"{last} ({n} test functions" + ("" if n >= 3 else "; aim for at least 3") + ")"))
    if skip_run:
        results.append((WARN, "run_analysis.py runs", "skipped (--skip-run)"))
    elif (work / "run_analysis.py").exists():
        proc = run([sys.executable, "run_analysis.py"], work, env)
        results.append((PASS, "run_analysis.py runs", "from a clean copy, exit code 0") if proc.returncode == 0
                       else (FAIL, "run_analysis.py runs", (proc.stderr.strip().splitlines() or ["failed"])[-1][:200]))
    if run_notebooks:
        bad = []
        for nb in sorted(work.rglob("*.ipynb")):
            if ".ipynb_checkpoints" in nb.parts:
                continue
            proc = run([sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute", "--output-dir", str(work / ".nbout"), str(nb)], nb.parent, env)
            if proc.returncode != 0:
                bad.append(nb.name)
        results.append((FAIL, "notebooks execute", "failed: " + ", ".join(bad)) if bad else (PASS, "notebooks execute", "Restart & Run All works"))
    return results


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("project", type=Path, help="path to the project folder")
    parser.add_argument("--skip-run", action="store_true", help="do not execute run_analysis.py")
    parser.add_argument("--run-notebooks", action="store_true", help="also execute every notebook")
    args = parser.parse_args(argv)

    root = args.project.resolve()
    if not root.is_dir():
        print(f"error: {root} is not a folder", file=sys.stderr)
        return 2

    results = check_readme(root) + check_structure(root) + check_paths(root) + check_notebook_outputs(root)
    with tempfile.TemporaryDirectory(prefix="project_doctor_") as tmp:
        work = Path(tmp) / root.name
        shutil.copytree(root, work, ignore=IGNORE)
        results += check_tests_and_run(work, args.skip_run, args.run_notebooks)

    width = max(len(name) for _, name, _ in results)
    print(f"\nProject doctor: {root.name}\n")
    for status, name, detail in results:
        print(f"  {status} {name:<{width}}  {detail}".rstrip())
    fails = sum(1 for s, _, _ in results if s == FAIL)
    warns = sum(1 for s, _, _ in results if s == WARN)
    print(f"\n{len(results) - fails - warns} passed, {warns} to improve, {fails} to fix.")
    if fails:
        print("Fix the ❌ items, then run the doctor again.")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
