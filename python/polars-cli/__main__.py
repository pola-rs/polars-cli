"""
Setup borrowed from ruff:
https://github.com/astral-sh/ruff/blob/main/python/ruff/__main__.py
"""
import os
import subprocess
import sys
import sysconfig
from pathlib import Path


def find_polars_bin() -> Path:
    """Return the Polars CLI binary path."""

    polars_exe = "polars" + sysconfig.get_config_var("EXE")

    path = Path(sysconfig.get_path("scripts")) / polars_exe
    if path.is_file():
        return path

    if sys.version_info >= (3, 10):
        user_scheme = sysconfig.get_preferred_scheme("user")
    elif os.name == "nt":
        user_scheme = "nt_user"
    elif sys.platform == "darwin" and sys._framework:
        user_scheme = "osx_framework_user"
    else:
        user_scheme = "posix_user"

    path = Path(sysconfig.get_path("scripts", scheme=user_scheme)) / polars_exe
    if path.is_file():
        return path

    raise FileNotFoundError(path)


if __name__ == "__main__":
    polars = find_polars_bin()
    completed_process = subprocess.run([polars, *sys.argv[1:]])
    sys.exit(completed_process.returncode)
