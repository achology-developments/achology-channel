#!/usr/bin/env python3
"""Picture guard: keeps working pictures out of the shared project folder.

Kain, S489, 25 November 2026: each computer has its own Achology Workbench in the
home folder (outside iCloud, cleared daily by com.achology.workbench); the shared
folder holds finished work only.

PreToolUse on Write/Edit: refuses a picture written into the shared folder unless
it is going to a picture home (a folder named images, page images, assets, pages,
an archive, or one on the allow list in folder_check.py).

PostToolUse on Bash: when a command looks like it makes pictures, finds pictures
made in the shared folder in the last ten minutes outside a picture home and tells
the Claude to move them to the workbench. It never moves or deletes anything itself,
because a file here may have arrived from the other computer through iCloud.
"""
import json
import os
import re
import subprocess
import sys

ROOT = "/Users/kainramsay/Documents/CLAUDE | Anthropic Ai"
WB = os.path.expanduser("~/Achology Workbench")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from folder_check import IMAGE_EXT, image_is_home, SKIP_DIRS  # noqa: E402

MSG = (
    "PICTURE GUARD (Kain, S489): working pictures never go in the shared project folder. "
    f"Save screenshots, renders and test pictures in {WB} instead (it clears itself after 7 days). "
    "Only a finished picture goes in the project, and only into its picture home "
    "(an images, page images, assets or pages folder)."
)


def at_home(path):
    rel = os.path.relpath(os.path.dirname(path), ROOT)
    parts = [] if rel == "." else rel.split(os.sep)
    return image_is_home(parts)


def inside_root(path):
    try:
        return os.path.commonpath([os.path.realpath(path), os.path.realpath(ROOT)]) == os.path.realpath(ROOT)
    except ValueError:
        return False


def is_picture(path):
    return os.path.splitext(path)[1].lower() in IMAGE_EXT


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "pre"
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    tool = data.get("tool_name", "")
    inp = data.get("tool_input", {}) or {}

    if mode == "pre" and tool in ("Write", "Edit", "MultiEdit"):
        p = inp.get("file_path", "")
        if p and is_picture(p) and inside_root(p) and not at_home(p):
            print(f"{MSG}\nRefused: {p}", file=sys.stderr)
            return 2
        return 0

    if mode == "post" and tool == "Bash":
        cmd = inp.get("command", "")
        if not re.search(r"screenshot|\.png|\.jpe?g|\.webp|\.gif|playwright|render|chrome|pdftoppm|sips|ffmpeg|magick|convert", cmd, re.I):
            return 0
        try:
            out = subprocess.run(
                ["find", ROOT, "(", *sum([["-name", d, "-o"] for d in SKIP_DIRS], [])[:-1], ")", "-prune", "-o",
                 "-type", "f", "-mmin", "-10", "-print"],
                capture_output=True, text=True, timeout=40,
            ).stdout.splitlines()
        except Exception:
            return 0
        loose = [p for p in out if is_picture(p) and not at_home(p)]
        if loose:
            shown = "\n".join(loose[:20])
            more = f"\n...and {len(loose) - 20} more" if len(loose) > 20 else ""
            print(f"{MSG}\nThis command left pictures in the project. Move each one you made to the workbench now. A picture this command did not make may have come from the other computer through iCloud: leave it and tell the other seat through the channel.\n{shown}{more}",
                  file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
