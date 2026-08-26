#!/usr/bin/env python3
"""Validate SCHEDULE.md tutorial claims and report what's still available.

Usage (from the repo root):  just check   (or: python3 scripts/check_schedule.py)

Checks:
  - claim cells parse as "NN · Name" or "NN · Name & Name"
  - topic numbers correspond to files in topics/
  - no topic is claimed more than once
  - at most 2 presenters per tutorial, at most 3 claims per day
  - no claims on Labor Day, dates fall on Mon/Wed and match the Day column
Warns if the same presenter name appears in more than one claim.
Then prints unclaimed topics and remaining open slots.
"""

import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCHEDULE = ROOT / "SCHEDULE.md"
TOPICS_DIR = ROOT / "topics"
LABOR_DAY = datetime.date(2026, 9, 7)

CLAIM_RE = re.compile(r"^(\d{1,2})\s*[·\-–—:.]\s*(.+)$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def load_topics():
    topics = {}
    for path in sorted(TOPICS_DIR.glob("tutorial-*.md")):
        m = re.match(r"tutorial-(\d+)-", path.name)
        if m:
            topics[int(m.group(1))] = path.name
    return topics


def main():
    errors, warnings = [], []
    topics = load_topics()
    if not topics:
        sys.exit(f"error: no tutorial files found in {TOPICS_DIR}")

    claims = {}          # topic number -> (date, presenters)
    presenter_seen = {}  # lowercased name -> topic number
    open_slots = []      # (date, slot index)
    row_num = 0

    for line in SCHEDULE.read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or not DATE_RE.match(cells[0]):
            continue
        row_num += 1
        date = datetime.date.fromisoformat(cells[0])
        day_label, slots = cells[1], cells[2:5]
        weekday = date.strftime("%a")

        if weekday not in ("Mon", "Wed"):
            errors.append(f"{date}: falls on {weekday} — calls are Mon/Wed only")
        if day_label != weekday:
            errors.append(f"{date}: Day column says {day_label!r} but the date is a {weekday}")

        day_claims = 0
        for i, cell in enumerate(slots, start=1):
            if not cell or set(cell) <= {"—", "-"} or "no call" in cell.lower():
                if date != LABOR_DAY and not cell:
                    open_slots.append((date, i))
                continue
            if date == LABOR_DAY:
                errors.append(f"{date} slot {i}: claim on Labor Day (no call): {cell!r}")
                continue
            m = CLAIM_RE.match(cell)
            if not m:
                errors.append(f"{date} slot {i}: unparseable claim {cell!r} "
                              f"(expected 'NN · Name & Name')")
                continue
            num = int(m.group(1))
            presenters = [p.strip() for p in re.split(r"\s*(?:&|,| and )\s*", m.group(2)) if p.strip()]
            if num not in topics:
                errors.append(f"{date} slot {i}: topic {num:02d} does not exist in topics/")
                continue
            if not 1 <= len(presenters) <= 2:
                errors.append(f"{date} slot {i}: topic {num:02d} has {len(presenters)} presenters "
                              f"(max 2 per tutorial)")
            if num in claims:
                prev_date, _ = claims[num]
                errors.append(f"{date} slot {i}: topic {num:02d} already claimed on {prev_date}")
            else:
                claims[num] = (date, presenters)
                for p in presenters:
                    key = p.lower()
                    if key in presenter_seen:
                        warnings.append(f"{p!r} appears on topic {presenter_seen[key]:02d} "
                                        f"and topic {num:02d}")
                    else:
                        presenter_seen[key] = num
            day_claims += 1
        if day_claims > 3:
            errors.append(f"{date}: {day_claims} claims (max 3 slots per day)")

    if row_num == 0:
        sys.exit(f"error: no schedule rows found in {SCHEDULE}")

    for e in errors:
        print(f"ERROR   {e}")
    for w in warnings:
        print(f"WARNING {w}")

    print(f"\n{len(claims)} of {len(topics)} topics claimed; "
          f"{len(open_slots)} open slots remain.")
    unclaimed = sorted(set(topics) - set(claims))
    if unclaimed:
        print("\nAvailable topics:")
        for num in unclaimed:
            print(f"  {num:02d}  topics/{topics[num]}")
    if claims:
        print("\nClaimed:")
        for num, (date, presenters) in sorted(claims.items(), key=lambda kv: kv[1][0]):
            print(f"  {date}  {num:02d}  {' & '.join(presenters)}")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
