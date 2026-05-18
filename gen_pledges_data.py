#!/usr/bin/env python3
"""
Write data/pledges_stats.json from the pledges CSV.
Hugo reads this file at build time via site.Data.pledges_stats.
Run from the repo root:  python3 gen_pledges_data.py
"""

import json, pathlib, compute_pledges

ROOT = pathlib.Path(__file__).parent

s = compute_pledges.stats(compute_pledges.load())
out = {
    "neighbors": s["count"],
    "pledged":   compute_pledges.fmt(s["total"]),
}

dest = ROOT / "data" / "pledges_stats.json"
dest.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(f"Written → {dest}  ({out})")
