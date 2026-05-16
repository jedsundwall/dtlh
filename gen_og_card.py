#!/usr/bin/env python3
"""
Generate a branded OpenGraph card PNG (1200×630) showing pledger count and total pledged.
Run from the repo root:  python3 gen_og_card.py
Output:  static/og-card.png
"""

import base64, subprocess, sys, pathlib

ROOT     = pathlib.Path(__file__).parent
FONT_DIR = ROOT / "static" / "fonts"

def b64font(path):
    return base64.b64encode(path.read_bytes()).decode()

germania_b64  = b64font(FONT_DIR / "germania-one-regular.woff2")
ss4_roman_b64 = b64font(FONT_DIR / "source-serif-4-variable-roman.woff2")
ss4_italic_b64 = b64font(FONT_DIR / "source-serif-4-variable-italic.woff2")

# ── Read milestone values from Hugo frontmatter ───────────────────────────────
import re

frontmatter_text = (ROOT / "content" / "_index.md").read_text(encoding="utf-8")
neighbors_match  = re.search(r"^milestone_neighbors:\s*(\d+)", frontmatter_text, re.MULTILINE)
pledged_match    = re.search(r'^milestone_pledged:\s*"([^"]+)"', frontmatter_text, re.MULTILINE)

if not neighbors_match or not pledged_match:
    sys.exit("Could not parse milestone values from content/_index.md frontmatter")

count_str = neighbors_match.group(1)
total_str = pledged_match.group(1)

# ── Layout constants ──────────────────────────────────────────────────────────
W, H   = 1200, 630
PAD    = 64
CREAM  = "#F1ECE2"
PINK   = "#B53050"
INK    = "#0D0B0A"
MUTED  = "#3A2E28"

# Left column: title — divider pushed right so "Loyal Heights" has room
DIVIDER_X   = 610
LEFT_CX     = (PAD + DIVIDER_X) // 2          # 337
RIGHT_CX    = (DIVIDER_X + W - PAD) // 2      # 905

WM_SIZE     = 76   # fits comfortably in left column
# Vertically center the two-line wordmark in the card
WM_LINE_H   = WM_SIZE * 1.10               # line-to-line spacing
WM_BLOCK_H  = WM_SIZE + WM_LINE_H          # total visual block height
WM_Y1       = (H - WM_BLOCK_H) / 2 + WM_SIZE * 0.82   # "Downtown" baseline
WM_Y2       = WM_Y1 + WM_LINE_H                        # "Loyal Heights" baseline

# Right column: two stacked stats, split at card mid-height
NUM_SIZE    = 130
LABEL_SIZE  = 26

MID_Y       = H // 2   # 315 — horizontal rule splitting right side

# Upper stat: count — sits in top half, label clears the rule with room
NUM1_Y      = MID_Y - 90          # number baseline
LABEL1_Y    = NUM1_Y + 38         # label below number, well above divider

# Lower stat: total — sits in bottom half
NUM2_Y      = MID_Y + NUM_SIZE * 0.80 + 30   # number baseline
LABEL2_Y    = NUM2_Y + 38

# Vertical rule x-position and extents
VRULE_Y1 = PAD
VRULE_Y2 = H - PAD

# Horizontal rule in right column between the two stats
HRULE_X1 = DIVIDER_X + 36
HRULE_X2 = W - PAD

# ── Build SVG ─────────────────────────────────────────────────────────────────
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
      @font-face {{
        font-family: "Source Serif 4";
        src: url("data:font/woff2;base64,{ss4_italic_b64}") format("woff2");
        font-weight: 200 900; font-style: italic;
      }}
    </style>
  </defs>

  <!-- background -->
  <rect width="{W}" height="{H}" fill="{CREAM}"/>

  <!-- LEFT: wordmark, vertically centered -->
  <text font-family="'Germania One',serif" font-size="{WM_SIZE}"
        fill="{PINK}" x="{LEFT_CX}" y="{WM_Y1:.1f}"
        text-anchor="middle" letter-spacing="0.005em">Downtown</text>
  <text font-family="'Germania One',serif" font-size="{WM_SIZE}"
        fill="{PINK}" x="{LEFT_CX}" y="{WM_Y2:.1f}"
        text-anchor="middle" letter-spacing="0.005em">Loyal Heights</text>

  <!-- vertical rule dividing left title from right stats -->
  <line x1="{DIVIDER_X}" x2="{DIVIDER_X}" y1="{VRULE_Y1}" y2="{VRULE_Y2}"
        stroke="{MUTED}" stroke-width="1" stroke-opacity="0.25"/>

  <!-- horizontal rule splitting the two right-column stats -->
  <line x1="{HRULE_X1}" x2="{HRULE_X2}" y1="{MID_Y}" y2="{MID_Y}"
        stroke="{MUTED}" stroke-width="1" stroke-opacity="0.25"/>

  <!-- RIGHT upper: neighbor count -->
  <text font-family="'Germania One',serif" font-size="{NUM_SIZE}"
        fill="{PINK}" x="{RIGHT_CX}" y="{NUM1_Y:.1f}"
        text-anchor="middle">{count_str}</text>
  <text font-family="'Source Serif 4',Georgia,serif"
        font-style="italic" font-weight="600" font-size="{LABEL_SIZE}"
        fill="{MUTED}" x="{RIGHT_CX}" y="{LABEL1_Y:.1f}"
        text-anchor="middle">neighbors pledged</text>

  <!-- RIGHT lower: total pledged -->
  <text font-family="'Germania One',serif" font-size="{NUM_SIZE}"
        fill="{PINK}" x="{RIGHT_CX}" y="{NUM2_Y:.1f}"
        text-anchor="middle">{total_str}</text>
  <text font-family="'Source Serif 4',Georgia,serif"
        font-style="italic" font-weight="600" font-size="{LABEL_SIZE}"
        fill="{MUTED}" x="{RIGHT_CX}" y="{LABEL2_Y:.1f}"
        text-anchor="middle">committed to our neighborhood</text>

</svg>"""

# ── Write SVG & render PNG ────────────────────────────────────────────────────
svg_path = ROOT / "og-card.svg"
png_path = ROOT / "static" / "og-card.png"

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

print(f"PNG written  → {png_path}  ({W}×630)")
