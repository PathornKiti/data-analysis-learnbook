"""Run YOUR tests against the correct code and against 9 deliberately buggy versions.

    python checker/check_my_tests.py

Good tests pass on the correct code and FAIL on every buggy version ("caught").
A buggy version your tests don't notice "survived": write a test that would have caught it.
"""
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

MUTANTS = {
    "pc_wrong_base": "percent_change divides by the NEW value instead of the old",
    "pc_no_percent": "percent_change forgets to multiply by 100",
    "pc_zero_no_raise": "percent_change returns inf instead of raising ValueError when old == 0",
    "iqr_factor_3": "iqr_outliers uses 3.0 * IQR fences instead of 1.5",
    "iqr_boundary_inclusive": "iqr_outliers treats a value exactly on a fence as an outlier",
    "iqr_only_high": "iqr_outliers ignores unusually LOW values",
    "sm_count": "share_missing returns the count instead of the fraction",
    "sm_inverted": "share_missing returns the share that is present instead of missing",
    "sm_empty_nan": "share_missing returns NaN instead of 0.0 for an empty DataFrame",
}


def run_tests(mutant: str = ""):
    env = dict(os.environ, RK_MUTANT=mutant, PYTHONPATH=os.pathsep.join([str(ROOT / "src"), str(HERE)]))
    return subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-x", "--no-header", "-p", "no:cacheprovider",
         "-p", "mutants_plugin", str(ROOT / "tests" / "test_student.py")],
        cwd=ROOT, env=env, capture_output=True, text=True,
    )


def main() -> int:
    base = run_tests()
    if base.returncode != 0:
        print("❌ Your tests must pass on the CORRECT code first. Fix this before anything else:\n")
        print((base.stdout + base.stderr)[-1500:])
        return 1
    n_tests = sum(1 for line in (ROOT / "tests" / "test_student.py").read_text().splitlines() if line.startswith("def test_"))
    print(f"✅ {n_tests} tests pass on the correct code.\n")

    survived = []
    for name, description in MUTANTS.items():
        result = run_tests(name)
        caught = result.returncode == 1                       # 1 = tests ran and at least one failed
        print(f"{'✅ caught  ' if caught else '❌ SURVIVED'}  {name:24s} {description}")
        if not caught:
            survived.append(name)

    print()
    if survived:
        print(f"{len(MUTANTS) - len(survived)}/{len(MUTANTS)} bugs caught. Add tests for the survivors above.")
        return 1
    print(f"🎉 All {len(MUTANTS)} bugs caught. Your tests do real work.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
