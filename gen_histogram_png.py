#!/usr/bin/env python3
"""
Generate a branded histogram PNG suitable for LinkedIn (1200×675).
Run from the repo root:  python3 gen_histogram_png.py
Output:  histogram-linkedin.png
"""

import csv, base64, subprocess, sys, pathlib

# ── Fonts ────────────────────────────────────────────────────────────────────
ROOT = pathlib.Path(__file__).parent
FONT_DIR = ROOT / "static" / "fonts"

def b64font(path):
    return base64.b64encode(path.read_bytes()).decode()

germania_b64   = b64font(FONT_DIR / "germania-one-regular.woff2")
ss4_roman_b64  = b64font(FONT_DIR / "source-serif-4-variable-roman.woff2")

# ── Parse CSV ─────────────────────────────────────────────────────────────────
amounts = []
with open(ROOT / "assets" / "data" / "pledges.csv") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
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

count = len(amounts)
total = sum(amounts)
mean  = total / count if count else 0
sa    = sorted(amounts)
mid   = count // 2
median = (sa[mid-1] + sa[mid]) / 2 if count % 2 == 0 else sa[mid]

# ── Bucket ────────────────────────────────────────────────────────────────────
BUCKET_LABELS = ["&lt;$1K","$1K&#x2013;5K","$5K&#x2013;10K","$10K&#x2013;25K",
                 "$25K&#x2013;50K","$50K&#x2013;100K","$100K&#x2013;500K","$500K+"]
EDGES = [1000, 5000, 10000, 25000, 50000, 100000, 500000]
buckets = [0] * 8
for a in amounts:
    idx = next((j for j, e in enumerate(EDGES) if a < e), 7)
    buckets[idx] += 1
max_count = max(buckets) if buckets else 1

def fmt(v):
    if v >= 1_000_000: return f"${v/1_000_000:.2f}M"
    if v >= 1_000:     return f"${v/1_000:.0f}K"
    return f"${v:.0f}"

# ── Layout ────────────────────────────────────────────────────────────────────
W, H     = 1200, 720
PX       = 64          # horizontal padding
PY_TOP   = 40

# Wordmark geometry comes first so RULE_Y can clear the actual text baseline
WM_SIZE    = 62
WM_LINE1_Y = PY_TOP + WM_SIZE * 0.9          # baseline of "Downtown"   ≈ 96
WM_LINE2_Y = WM_LINE1_Y + WM_SIZE * 0.95     # baseline of "Loyal Heights" ≈ 155
RULE_Y     = WM_LINE2_Y + 24                  # clear the descenders       ≈ 179

STATS_Y    = RULE_Y + 36      # top of stats block
STATS_H    = 80
CHART_TOP  = STATS_Y + STATS_H + 24
CHART_BOT  = H - 100          # room for tick labels + caption + bottom pad
CHART_H    = CHART_BOT - CHART_TOP
CHART_X    = PX
CHART_W    = W - 2 * PX
N          = 8
SLOT_W     = CHART_W / N
BAR_W      = int(SLOT_W * 0.72)
BAR_GAP    = (SLOT_W - BAR_W) / 2

# ── Colors / tokens ──────────────────────────────────────────────────────────
CREAM     = "#F1ECE2"
PINK      = "#B53050"
INK       = "#0D0B0A"
MUTED     = "#3A2E28"
RULE_CLR  = "rgba(42,33,27,0.15)"

# ── Build SVG ─────────────────────────────────────────────────────────────────
bars = []
for i, label in enumerate(BUCKET_LABELS):
    c = buckets[i]
    bh = int((c / max_count) * CHART_H) if max_count else 0
    x  = CHART_X + i * SLOT_W + BAR_GAP
    y  = CHART_BOT - bh
    cx = x + BAR_W / 2

    if c > 0:
        bars.append(f'<rect fill="{PINK}" x="{x:.1f}" y="{y:.1f}" '
                    f'width="{BAR_W}" height="{bh}" rx="2"/>')
        bars.append(f'<text font-family="\'Courier New\',monospace" font-size="16" font-weight="bold" '
                    f'fill="{INK}" x="{cx:.1f}" y="{y-8:.1f}" text-anchor="middle">{c}</text>')

    bars.append(f'<text font-family="\'Courier New\',monospace" font-size="16" font-weight="bold" '
                f'letter-spacing="0.04em" fill="{INK}" '
                f'x="{cx:.1f}" y="{CHART_BOT+22:.1f}" text-anchor="middle">{label}</text>')

stats_items = [
    ("Pledges",      str(count)),
    ("Total raised", fmt(total)),
    ("Mean",         fmt(mean)),
    ("Median",       fmt(median)),
]
stat_col_w = CHART_W / 4
stats_svg  = []
for si, (label, val) in enumerate(stats_items):
    sx = CHART_X + si * stat_col_w
    # top rule
    stats_svg.append(f'<line x1="{sx:.1f}" x2="{sx + stat_col_w - 12:.1f}" '
                     f'y1="{STATS_Y:.1f}" y2="{STATS_Y:.1f}" '
                     f'stroke="{MUTED}" stroke-width="1" stroke-opacity="0.35"/>')
    # label
    stats_svg.append(f'<text font-family="\'Courier New\',monospace" font-size="16" font-weight="bold" '
                     f'letter-spacing="0.16em" fill="{INK}" '
                     f'x="{sx:.1f}" y="{STATS_Y+20:.1f}">{label.upper()}</text>')
    # value — Germania One for the big number
    stats_svg.append(f'<text font-family="\'Germania One\',serif" font-size="32" '
                     f'fill="{INK}" x="{sx:.1f}" y="{STATS_Y+58:.1f}">{val}</text>')

svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{W}" height="{H}" viewBox="0 0 {W} {H}">

  <defs>
    <style>
      @font-face {{
        font-family: "Germania One";
        src: url("data:font/woff2;base64,{germania_b64}") format("woff2");
        font-weight: 400; font-style: normal;
      }}
      @font-face {{
        font-family: "Source Serif 4";
        src: url("data:font/woff2;base64,{ss4_roman_b64}") format("woff2");
        font-weight: 200 900; font-style: normal;
      }}
    </style>
  </defs>

  <!-- background -->
  <rect width="{W}" height="{H}" fill="{CREAM}"/>

  <!-- wordmark -->
  <text font-family="'Germania One',serif" font-size="{WM_SIZE}"
        fill="{PINK}" x="{W/2}" y="{WM_LINE1_Y:.1f}"
        text-anchor="middle" letter-spacing="0.005em">Downtown</text>
  <text font-family="'Germania One',serif" font-size="{WM_SIZE}"
        fill="{PINK}" x="{W/2}" y="{WM_LINE2_Y:.1f}"
        text-anchor="middle" letter-spacing="0.005em">Loyal Heights</text>

  <!-- divider rule below wordmark -->
  <line x1="{CHART_X}" x2="{W - PX}" y1="{RULE_Y}" y2="{RULE_Y}"
        stroke="{MUTED}" stroke-width="1" stroke-opacity="0.25"/>

  <!-- stats -->
  {''.join(stats_svg)}

  <!-- chart baseline -->
  <line x1="{CHART_X}" x2="{W - PX}" y1="{CHART_BOT}" y2="{CHART_BOT}"
        stroke="{MUTED}" stroke-width="1" stroke-opacity="0.35"/>

  <!-- bars + labels -->
  {''.join(bars)}

  <!-- caption bottom-left -->
  <text font-family="'Source Serif 4',Georgia,serif" font-style="italic" font-weight="bold"
        font-size="16" fill="{MUTED}"
        x="{CHART_X}" y="{H - 18}" text-anchor="start">
    Pledges to date, by amount (excluding zero-pledge sign-ups)
  </text>
</svg>"""

# ── Write SVG & render PNG ─────────────────────────────────────────────────────
svg_path = ROOT / "histogram-linkedin.svg"
png_path = ROOT / "histogram-linkedin.png"

svg_path.write_text(svg, encoding="utf-8")
print(f"SVG written → {svg_path}")

result = subprocess.run(
    ["rsvg-convert", "-w", str(W), "-h", str(H), "-o", str(png_path), str(svg_path)],
    capture_output=True, text=True
)
if result.returncode != 0:
    print("rsvg-convert failed, trying inkscape…", file=sys.stderr)
    print(result.stderr, file=sys.stderr)
    result2 = subprocess.run(
        ["inkscape", f"--export-filename={png_path}",
         f"--export-width={W}", f"--export-height={H}", str(svg_path)],
        capture_output=True, text=True
    )
    if result2.returncode != 0:
        print("inkscape also failed:", result2.stderr, file=sys.stderr)
        sys.exit(1)

print(f"PNG written  → {png_path}  ({W}×{H})")
