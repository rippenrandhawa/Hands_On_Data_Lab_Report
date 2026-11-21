"""verify_environment.py -- Task 2 environment verification.

Run from the project root with the virtual environment active:

    python verify_environment.py

Prints a clear PASS/FAIL line for every check and raises AssertionError
if any required check fails, so it can also be used in automated setup.
"""

import importlib.metadata as metadata
import sys
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd
import scipy
import seaborn

PROJECT_ROOT = Path.cwd()
EXPECTED_FOLDERS = ["data", "outputs"]
EXPECTED_FILES = ["Hands_On_Data_Lab.ipynb", "README.md", "requirements.txt"]
REQUIRED_LIBRARIES = {
    "numpy": np,
    "pandas": pd,
    "matplotlib": matplotlib,
    "seaborn": seaborn,
    "scipy": scipy,
}

results = []


def check(name, condition, detail=""):
    """Print a PASS/FAIL line and record the result."""
    status = "PASS" if condition else "FAIL"
    line = f"[{status}] {name}"
    if detail:
        line += f" -- {detail}"
    print(line)
    results.append((name, bool(condition), detail))


print("=" * 70)
print("HANDS-ON DATA LAB -- ENVIRONMENT VERIFICATION")
print("=" * 70)

print(f"\nPython version    : {sys.version.split()[0]}")
print(f"Working directory : {PROJECT_ROOT}")

print("\n--- Required libraries ---")
for name, module in REQUIRED_LIBRARIES.items():
    print(f"{name:<13} {module.__version__}")
try:
    jupyterlab_version = metadata.version("jupyterlab")
except metadata.PackageNotFoundError:
    jupyterlab_version = None
print(f"{'jupyterlab':<13} {jupyterlab_version or 'NOT INSTALLED'}")

print("\n--- Project folders ---")
for folder in EXPECTED_FOLDERS:
    check(f"folder '{folder}/' exists", (PROJECT_ROOT / folder).is_dir())

print("\n--- Key project files ---")
for name in EXPECTED_FILES:
    check(f"file '{name}' exists", (PROJECT_ROOT / name).is_file())

print("\n--- Version sanity ---")
check("pandas is version 2.x", pd.__version__.startswith("2."), pd.__version__)
check("numpy is installed", numpy_ok := np.__version__ is not None, np.__version__)
check("jupyterlab is installed", jupyterlab_version is not None,
      jupyterlab_version or "missing")

print("\n--- Reproducibility check: np.random.default_rng(42) ---")
draw_one = np.random.default_rng(42).integers(0, 1000, size=5)
draw_two = np.random.default_rng(42).integers(0, 1000, size=5)
print("Draw 1:", draw_one)
print("Draw 2:", draw_two)
check("seeded draws are identical", np.array_equal(draw_one, draw_two))

print("\n" + "=" * 70)
failed = [name for name, ok, _ in results if not ok]
if failed:
    print(f"RESULT: FAIL -- {len(failed)} check(s) failed: {', '.join(failed)}")
    raise AssertionError(f"Environment verification failed: {failed}")
print(f"RESULT: PASS -- all {len(results)} checks succeeded.")
print("=" * 70)
