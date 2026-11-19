"""Copy the finished news image to the grader's output folder.

The image is entry.png beside this file. The program only copies
bytes, so both runs write exactly the same file. It uses only the
Python standard library, and it needs no network.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

SOURCE = HERE / "entry.png"
if not SOURCE.is_file():
    raise SystemExit("entry.png is missing beside main.py")

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SOURCE, OUT / "entry.png")
