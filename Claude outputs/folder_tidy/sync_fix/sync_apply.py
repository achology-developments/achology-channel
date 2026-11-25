#!/usr/bin/env python3
"""Make the iMac's shared folder match the iMac Pro's, by replaying the iMac Pro's own tidy log.

Why (Chat, S489, 25 November 2026): iCloud carried the iMac's changes to the iMac Pro, but not the
iMac Pro's step 2 moves to the iMac (the iMac counted 44,495, the iMac Pro 30,282). Kain's ruling of
the truth: the iMac Pro's tidied tree. This script replays imac_pro_MOVE_LOG.tsv, line by line, and
only acts where the iMac Pro's current tree (imac_pro_tree.txt.gz) proves the thing is still gone there.
It never deletes: anything removed goes to the iMac's own holding folder.

Usage:  python3 sync_apply.py            dry run, prints what it would do
        python3 sync_apply.py --apply    does it, and writes sync_apply_log.tsv beside the holding
"""
import gzip
import os
import shutil
import sys

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "Documents", "CLAUDE | Anthropic Ai")
LOG_ROOT = "/Users/kainramsay/Documents/CLAUDE | Anthropic Ai"
HOLD = os.path.join(HOME, "Folder Tidy Holding 25 November 2026 (iMac)", "from iMac Pro log")
HERE = os.path.dirname(os.path.abspath(__file__))
APPLY = "--apply" in sys.argv


def rel(p):
    if p.startswith(LOG_ROOT + "/"):
        return p[len(LOG_ROOT) + 1:]
    return None


def main():
    with gzip.open(os.path.join(HERE, "imac_pro_tree.txt.gz"), "rt") as f:
        tree = set(line.rstrip("\n") for line in f)
    prefixes = set()
    for t in tree:
        parts = t.split("/")
        for i in range(1, len(parts)):
            prefixes.add("/".join(parts[:i]))

    def gone_on_pro(r):
        return r not in tree and r not in prefixes

    counts = {}
    out = []

    def note(kind, *a):
        counts[kind] = counts.get(kind, 0) + 1
        out.append("\t".join((kind,) + a))

    for line in open(os.path.join(HERE, "imac_pro_MOVE_LOG.tsv")):
        f = line.rstrip("\n").split("\t")
        op = f[0]
        src = rel(f[1]) if len(f) > 1 else None
        dst = rel(f[2]) if len(f) > 2 else None
        if op == "CREATE":
            continue
        if src is None:
            note("SKIP-outside-root", f[1] if len(f) > 1 else "")
            continue
        s = os.path.join(ROOT, src)
        if not os.path.lexists(s):
            note("ALREADY", src)
            continue
        if not gone_on_pro(src):
            note("KEEP-present-on-pro", src)
            continue
        if op in ("MOVE", "RENAME") and dst is not None:
            d = os.path.join(ROOT, dst)
            if not os.path.lexists(d):
                note("MOVE", src, dst)
                if APPLY:
                    os.makedirs(os.path.dirname(d), exist_ok=True)
                    shutil.move(s, d)
                continue
            if os.path.isdir(s) and os.path.isdir(d):
                # Both exist: move across only what the destination lacks, hold the rest.
                for base, dirs, files in os.walk(s):
                    for n in files:
                        fs = os.path.join(base, n)
                        fd = os.path.join(d, os.path.relpath(fs, s))
                        if not os.path.lexists(fd):
                            note("MERGE", os.path.relpath(fs, ROOT), os.path.relpath(fd, ROOT))
                            if APPLY:
                                os.makedirs(os.path.dirname(fd), exist_ok=True)
                                shutil.move(fs, fd)
                op = "HOLD"  # what is left of the old folder goes to holding
            else:
                op = "HOLD"
        if op in ("HOLD", "MOVE", "RENAME", "RMDIR-EMPTY"):
            note("HOLD", src)
            if APPLY and os.path.lexists(s):
                h = os.path.join(HOLD, src)
                os.makedirs(os.path.dirname(h), exist_ok=True)
                shutil.move(s, h)
            continue
        note("UNKNOWN-op", op, src)

    for k in sorted(counts):
        print(f"{k:<22}{counts[k]:>8}")
    print("APPLIED" if APPLY else "DRY RUN: nothing moved. Run with --apply to act.")
    target = os.path.join(os.path.dirname(HOLD) if APPLY else HERE, "sync_apply_log.tsv")
    with open(target, "w") as f:
        f.write("\n".join(out) + "\n")
    print("Log:", target)


if __name__ == "__main__":
    main()
