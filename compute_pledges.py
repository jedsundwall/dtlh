#!/usr/bin/env python3
"""Shared pledge computation — read the CSV and return stats."""

import csv, pathlib

ROOT = pathlib.Path(__file__).parent

def load():
    amounts = []
    with open(ROOT / "assets" / "data" / "pledges.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if not row:
                continue
            cell = row[0].strip().replace("$", "").replace(",", "").strip('"')
            if cell:
                try:
                    n = float(cell)
                    if n > 0:
                        amounts.append(n)
                except ValueError:
                    pass
    return amounts

def stats(amounts):
    count = len(amounts)
    total = sum(amounts)
    sa = sorted(amounts)
    mid = count // 2
    median = (sa[mid - 1] + sa[mid]) / 2 if count % 2 == 0 else sa[mid]
    mean = total / count if count else 0
    return {"count": count, "total": total, "mean": mean, "median": median}

def fmt(v):
    if v >= 1_000_000:
        return f"${v / 1_000_000:.2f}M"
    if v >= 1_000:
        return f"${v / 1_000:.0f}K"
    return f"${v:.0f}"
