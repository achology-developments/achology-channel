#!/bin/zsh
# Keeps each computer's tidy rules running by machine, never by a Claude remembering to.
#
#   workbench_keeper.sh          run once a day by macOS (com.achology.workbench):
#                                deletes anything on the Achology Workbench older than 7 days,
#                                then, if it is still over 5 GB, the oldest files until it is under.
#   workbench_keeper.sh count    run in the background at every Claude session start (hook in
#                                ~/.claude/settings.json): counts mess in the shared project folder.
#                                macOS does not let the daily job read Documents, so the count runs
#                                from Claude, which can.
#
# Each writes one line to this computer's health files in the channel, which Chat reads at every open:
#   heartbeat/<computer>.workbench.txt   and   heartbeat/<computer>.folders.txt

WB="$HOME/Achology Workbench"
LIMIT_KB=$((5 * 1024 * 1024))
ROOT="$HOME/Documents/CLAUDE | Anthropic Ai"
TOOLS="$HOME/.claude/achology-tidy"
HOST=$(scutil --get ComputerName 2>/dev/null | tr 'A-Z' 'a-z' | sed -E 's/[^a-z0-9]+/-/g; s/^-|-$//g')
HB="$HOME/achology-channel/heartbeat"
stamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
mkdir -p "$HB" "$WB"

if [[ "$1" == "count" ]]; then
  if ! ls "$ROOT/Claude Code (Projects)" >/dev/null 2>&1; then
    print -r -- "MESS  $stamp  folder check could not read the shared folder" > "$HB/${HOST}.folders.txt"
    exit 0
  fi
  total=$(/usr/bin/python3 "$TOOLS/folder_check.py" 2>/dev/null | awk '/^TOTAL/{print $2}')
  [[ -z "$total" ]] && total="failed"
  state="OK"; [[ "$total" != "0" ]] && state="MESS"
  print -r -- "$state  $stamp  folder check $total (full list: ~/.claude/achology-tidy/folder_check_report.json)" > "$HB/${HOST}.folders.txt"
  exit 0
fi

find "$WB" -mindepth 1 -type f -mtime +7 -delete
find "$WB" -mindepth 1 -type d -empty -delete
size_kb=$(du -sk "$WB" | cut -f1)
if (( size_kb > LIMIT_KB )); then
  find "$WB" -type f -exec stat -f '%m %N' {} + | sort -n | cut -d' ' -f2- | while IFS= read -r f; do
    rm -f -- "$f"
    size_kb=$(du -sk "$WB" | cut -f1)
    (( size_kb <= LIMIT_KB )) && break
  done
fi
size_mb=$(( $(du -sk "$WB" | cut -f1) / 1024 ))
state="OK"; (( size_mb > 5120 )) && state="OVER"
print -r -- "$state  $stamp  workbench ${size_mb} MB of 5120 MB, nothing older than 7 days" > "$HB/${HOST}.workbench.txt"
