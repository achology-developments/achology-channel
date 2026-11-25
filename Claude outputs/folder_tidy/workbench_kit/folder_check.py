#!/usr/bin/env python3
"""Folder check for CLAUDE | Anthropic Ai. Standard library only. Read-only: moves nothing.

Usage: python3 folder_check.py [root]   (exit 1 if anything is found)
Writes folder_check_report.json beside this script.
"""
import json
import os
import re
import sys
from collections import defaultdict

ROOT = "/Users/kainramsay/Documents/CLAUDE | Anthropic Ai"
SKIP_DIRS = {".git", ".claude", ".obsidian", "node_modules"}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}

# A picture is at home inside a folder with one of these names (case-insensitive,
# "archive" matches any name starting with it). Add owning folders here.
HOME_FOLDERS = {"page images", "images", "assets", "pages"}
ALLOWLIST = {
    "diagrams",
    "step_pages_webp",
}

COPY_NUM = re.compile(r" [2-9]$")
COPY_WORD = re.compile(r" \(?copy\)?(?= |\.|\)|$)", re.I)
SCRATCH = re.compile(r"(?<![a-z])(tmp|scratch|dummy|debug)(?![a-z])|_to_delete", re.I)

RULES = [
    "loose_images",
    "copy_names",
    "zip_beside_folder",
    "empty_folders",
    "scratch_names",
    "junk_files",
    "stale_000_notes",
]


def image_is_home(rel_dirs):
    for d in rel_dirs:
        low = d.lower()
        if low in HOME_FOLDERS or low.startswith("archive") or d in ALLOWLIST:
            return True
    return False


def walk(root):
    found = defaultdict(list)
    note_checks = []  # (dir, note path, note mtime, newest mtime in dir)

    def visit(path, rel_dirs):
        """Return newest mtime of any real file under path (excluding junk and 000__ notes)."""
        newest = 0.0
        try:
            entries = list(os.scandir(path))
        except OSError:
            return newest
        names = {e.name for e in entries}
        real = [e for e in entries if e.name != ".DS_Store"]
        if not real and path != root:
            found["empty_folders"].append(path)
        notes = []
        for e in entries:
            name = e.name
            full = e.path
            is_dir = e.is_dir(follow_symlinks=False)
            if name == ".DS_Store" or name == "__pycache__":
                found["junk_files"].append(full)
                continue
            stem, ext = (name, "") if is_dir else os.path.splitext(name)
            if COPY_NUM.search(stem) or COPY_WORD.search(name):
                base = COPY_NUM.sub("", stem) + ext
                found["copy_names"].append(
                    {"path": full, "original_beside": base in names and base != name}
                )
            if SCRATCH.search(name):
                found["scratch_names"].append(full)
            if is_dir:
                if name in SKIP_DIRS:
                    continue
                if name.startswith(".git"):
                    continue
                if e.is_symlink():
                    continue
                newest = max(newest, visit(full, rel_dirs + [name]))
            else:
                low = ext.lower()
                if low == ".zip" and stem in names:
                    try:
                        if os.path.isdir(os.path.join(path, stem)):
                            found["zip_beside_folder"].append(full)
                    except OSError:
                        pass
                if low in IMAGE_EXT and not image_is_home(rel_dirs):
                    found["loose_images"].append(full)
                if name.startswith("000__"):
                    notes.append(e)
                    continue
                try:
                    newest = max(newest, e.stat(follow_symlinks=False).st_mtime)
                except OSError:
                    pass
        for n in notes:
            try:
                note_checks.append((path, n.path, n.stat().st_mtime))
            except OSError:
                pass
        visit.newest[path] = newest
        return newest

    visit.newest = {}
    visit(root, [])
    for d, p, m in note_checks:
        if visit.newest.get(d, 0) > m:
            found["stale_000_notes"].append(p)
    return found


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else ROOT
    found = walk(root)
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "folder_check_report.json")
    with open(out, "w") as f:
        json.dump({r: found.get(r, []) for r in RULES}, f, indent=1)
    total = 0
    print(f"Folder check: {root}")
    print(f"{'rule':<22}{'count':>8}")
    for r in RULES:
        n = len(found.get(r, []))
        total += n
        print(f"{r:<22}{n:>8}")
        if r == "copy_names":
            real = sum(1 for c in found[r] if c["original_beside"])
            print(f"{'  (original beside)':<22}{real:>8}")
    print(f"{'TOTAL':<22}{total:>8}")
    print(f"Full list: {out}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
