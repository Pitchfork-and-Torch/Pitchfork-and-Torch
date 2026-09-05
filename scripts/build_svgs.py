"""Build dark/light neofetch SVGs with face ASCII from avatar."""
from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASCII = (ROOT / "assets" / "avatar-ascii.txt").read_text(encoding="utf-8").rstrip("\n")
LINES = ASCII.splitlines()
COLS = max((len(l) for l in LINES), default=0)

LEFT_X = 28
TOP_Y = 48
ASCII_FONT = 16.0
LINE_H = 17.5
PANEL_FONT = 18.0
USER_FONT = 21.0
HEAD_FONT = 16.0
ROW_GAP = 30

PORTRAIT_W = COLS * 0.60 * ASCII_FONT
PANEL_X = int(LEFT_X + PORTRAIT_W + 44)
CARD_W = max(1480, PANEL_X + 720)
CARD_H = 600


def escape_line(s: str) -> str:
    return html.escape(s, quote=False)


def ascii_tspans() -> str:
    parts = []
    for i, line in enumerate(LINES):
        y = TOP_Y + i * LINE_H
        parts.append(
            f'    <tspan x="{LEFT_X}" y="{y:.1f}">{escape_line(line)}</tspan>'
        )
    return "\n".join(parts)


def build(theme: str) -> str:
    if theme == "dark":
        frame_fill, frame_stroke = "#0d1117", "#30363d"
        ascii_fill = "#58a6ff"
        user_fill = "#58a6ff"
        sep_fill = "#8b949e"
        key_fill = "#ffa657"
        val_fill = "#c9d1d9"
        head_fill = "#8b949e"
        dots = [
            ("#ff7b72", CARD_W - 90, 48),
            ("#d2a8ff", CARD_W - 66, 48),
            ("#79c0ff", CARD_W - 42, 48),
            ("#7ee787", CARD_W - 90, 72),
            ("#ffa657", CARD_W - 66, 72),
            ("#8b949e", CARD_W - 42, 72),
        ]
    else:
        frame_fill, frame_stroke = "#ffffff", "#d0d7de"
        ascii_fill = "#0969da"
        user_fill = "#0969da"
        sep_fill = "#656d76"
        key_fill = "#bc4c00"
        val_fill = "#1f2328"
        head_fill = "#656d76"
        dots = [
            ("#cf222e", CARD_W - 90, 48),
            ("#8250df", CARD_W - 66, 48),
            ("#0969da", CARD_W - 42, 48),
            ("#1a7f37", CARD_W - 90, 72),
            ("#bc4c00", CARD_W - 66, 72),
            ("#656d76", CARD_W - 42, 72),
        ]

    rows = [
        ("OS", "Windows 11 · Linux · macOS"),
        ("Host", "jonbailey.xyz"),
        ("Kernel", "Builder · Musician · Operator"),
        ("Uptime", "25 days on GitHub"),
        ("Shell", "PowerShell · bash · zsh"),
        ("IDE", "VS Code · Cursor · Grok"),
        ("Languages.Programming", "Python, JavaScript, Dart, C, Shell"),
        ("Languages.Systems", "PowerShell, TypeScript, HTML/CSS"),
        ("Focus", "Network hardening · Privacy · RF research · AI agents"),
        ("Hobbies", "Music · Flipper Zero · Homelab · Local tools"),
    ]

    info_lines = []
    y0 = 128
    for i, (k, v) in enumerate(rows):
        y = y0 + i * ROW_GAP
        info_lines.append(
            f'  <text class="mono" x="{PANEL_X}" y="{y}">'
            f'<tspan class="key">{html.escape(k)}</tspan>'
            f'<tspan class="sep">: </tspan>'
            f'<tspan class="val">{html.escape(v)}</tspan></text>'
        )

    contact_y = y0 + len(rows) * ROW_GAP + 24
    contact = f'''  <text class="mono head" x="{PANEL_X}" y="{contact_y}">- Contact ------------------------------------------------</text>
  <text class="mono" x="{PANEL_X}" y="{contact_y + ROW_GAP}">
    <tspan class="key">Website</tspan><tspan class="sep">: </tspan><tspan class="val">https://jonbailey.xyz</tspan>
  </text>
  <text class="mono" x="{PANEL_X}" y="{contact_y + 2 * ROW_GAP}">
    <tspan class="key">GitHub</tspan><tspan class="sep">: </tspan><tspan class="val">@Pitchfork-and-Torch</tspan>
  </text>'''

    ascii_bottom = TOP_Y + len(LINES) * LINE_H + 36
    panel_bottom = contact_y + 2 * ROW_GAP + 44
    card_h = int(max(CARD_H, ascii_bottom, panel_bottom))

    dots_svg = "\n".join(
        f'  <circle cx="{x}" cy="{y}" r="10" fill="{c}"/>' for c, x, y in dots
    )

    return f'''<svg width="{CARD_W}" height="{card_h}" viewBox="0 0 {CARD_W} {card_h}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc">
  <title id="title">Pitchfork-and-Torch - GitHub profile</title>
  <desc id="desc">Neofetch-style system card with proportional ASCII portrait from GitHub avatar</desc>
  <style>
    .frame {{ fill: {frame_fill}; stroke: {frame_stroke}; stroke-width: 1; }}
    .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; font-size: {PANEL_FONT}px; }}
    .ascii {{ fill: {ascii_fill}; font-size: {ASCII_FONT}px; letter-spacing: 0; }}
    .user {{ fill: {user_fill}; font-weight: 700; font-size: {USER_FONT}px; }}
    .sep {{ fill: {sep_fill}; }}
    .key {{ fill: {key_fill}; font-weight: 700; }}
    .val {{ fill: {val_fill}; }}
    .head {{ fill: {head_fill}; font-size: {HEAD_FONT}px; }}
  </style>

  <rect class="frame" x="0.5" y="0.5" width="{CARD_W - 1}" height="{card_h - 1}" rx="12"/>

  <text class="mono ascii" xml:space="preserve">
{ascii_tspans()}
  </text>

  <text class="mono user" x="{PANEL_X}" y="56">jon@pitchfork-and-torch</text>
  <text class="mono sep" x="{PANEL_X}" y="84">-----------------------</text>

{chr(10).join(info_lines)}

{contact}

{dots_svg}
</svg>
'''


def main() -> None:
    dark = build("dark")
    light = build("light")
    (ROOT / "dark_mode.svg").write_text(dark, encoding="utf-8")
    (ROOT / "light_mode.svg").write_text(light, encoding="utf-8")
    print(
        f"wrote dark_mode.svg + light_mode.svg | {len(LINES)}x{COLS} | "
        f"ascii={ASCII_FONT} panel={PANEL_FONT} card={CARD_W}"
    )


if __name__ == "__main__":
    main()
