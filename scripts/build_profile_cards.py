"""Build local tokyonight pin/stats SVGs so the profile does not depend on Vercel."""
from __future__ import annotations

import html
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PINS = ROOT / "assets" / "pins"
STATS = ROOT / "assets" / "stats"

BG = "#1a1b27"
TITLE = "#70a5fd"
TEXT = "#38bdae"
ICON = "#bf91f3"
MUTED = "#a9b1d6"

LANG_COLOR = {
    "C": "#555555",
    "Python": "#3572A5",
    "PowerShell": "#012456",
    "JavaScript": "#f1e05a",
    "TypeScript": "#3178c6",
    "HTML": "#e34c26",
    "CSS": "#563d7c",
    "Shell": "#89e051",
    "Rust": "#dea584",
    "Go": "#00ADD8",
    "Dart": "#00B4AB",
}

FEATURED = [
    {
        "repo": "GrokLink-OS",
        "title": "GrokLink-OS",
        "desc": "From-scratch research RTOS for multi-radio portable hardware: gated agent, skills, GUI, PC bridge.",
    },
    {
        "repo": "netforge",
        "title": "netforge",
        "desc": "Cross-OS network performance and security hardening for Windows, Linux, and macOS.",
    },
    {
        "repo": "trench-coat",
        "title": "trench-coat",
        "desc": "Legal-first multi-hop privacy cloak with Tor-aware CLI and a cyberpunk control nexus.",
    },
    {
        "repo": "ghost-continuum",
        "title": "ghost-continuum",
        "desc": "Living digital immune system: Nexus, genomes, Home Shield, Merkle forensics.",
    },
]


def gh_json(args: list[str]) -> object:
    out = subprocess.check_output(["gh", *args], text=True, encoding="utf-8")
    return json.loads(out)


def ascii(s: str) -> str:
    return (
        (s or "")
        .replace("\u2014", "-")
        .replace("\u2013", "-")
        .replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
    )


def wrap(text: str, width: int = 52, max_lines: int = 2) -> list[str]:
    words = ascii(text).split()
    lines: list[str] = []
    cur = ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if len(lines) > max_lines:
        last = lines[max_lines - 1]
        if len(last) > width - 3:
            last = last[: width - 3]
        lines = lines[: max_lines - 1] + [last.rstrip(" .,") + "..."]
    return lines or [""]


def pin_svg(title: str, desc: str, lang: str, stars: int, forks: int) -> str:
    lines = wrap(desc)
    desc_svg = "\n  ".join(
        f'<text x="25" y="{70 + i * 14}" fill="{TEXT}" font-size="12" '
        f'font-family="Segoe UI, Ubuntu, Sans-Serif">{html.escape(line)}</text>'
        for i, line in enumerate(lines)
    )
    color = LANG_COLOR.get(lang, ICON)
    return f'''<svg width="400" height="120" viewBox="0 0 400 120" fill="none" xmlns="http://www.w3.org/2000/svg" role="img">
  <title>{html.escape(title)}</title>
  <rect width="400" height="120" rx="6" fill="{BG}"/>
  <g transform="translate(25, 32)" fill="{ICON}">
    <path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"/>
  </g>
  <text x="48" y="42" fill="{TITLE}" font-size="16" font-weight="600" font-family="Segoe UI, Ubuntu, Sans-Serif">{html.escape(title)}</text>
  {desc_svg}
  <circle cx="32" cy="102" r="5" fill="{color}"/>
  <text x="42" y="106" fill="{TEXT}" font-size="12" font-family="Segoe UI, Ubuntu, Sans-Serif">{html.escape(lang or "n/a")}</text>
  <g transform="translate(150, 94)" fill="{ICON}">
    <path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/>
  </g>
  <text x="170" y="106" fill="{TEXT}" font-size="12" font-family="Segoe UI, Ubuntu, Sans-Serif">{stars}</text>
  <g transform="translate(210, 94)" fill="{ICON}">
    <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 00.75-.75v-.878a2.25 2.25 0 111.5 0v.878A2.25 2.25 0 0110.25 8.25h-4.5A2.25 2.25 0 013.5 6.25v-.878a2.25 2.25 0 111.5 0zM5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm6.5 0a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM3.25 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zm9.5 0a.75.75 0 110-1.5.75.75 0 010 1.5z"/>
  </g>
  <text x="232" y="106" fill="{TEXT}" font-size="12" font-family="Segoe UI, Ubuntu, Sans-Serif">{forks}</text>
</svg>
'''


def stats_svg(stars: int, prs: int, issues: int, repos: int, followers: int) -> str:
    rows = [
        ("Total Stars", str(stars)),
        ("Total PRs", str(prs)),
        ("Total Issues", str(issues)),
        ("Public Repos", str(repos)),
        ("Followers", str(followers)),
    ]
    items = []
    for i, (k, v) in enumerate(rows):
        y = 62 + i * 22
        items.append(
            f'<text x="25" y="{y}" fill="{MUTED}" font-size="13" font-family="Segoe UI, Ubuntu, Sans-Serif">{html.escape(k)}</text>'
            f'<text x="390" y="{y}" text-anchor="end" fill="{TEXT}" font-size="13" font-weight="600" font-family="Segoe UI, Ubuntu, Sans-Serif">{html.escape(v)}</text>'
        )
    return f'''<svg width="415" height="195" viewBox="0 0 415 195" fill="none" xmlns="http://www.w3.org/2000/svg" role="img">
  <title>GitHub stats</title>
  <rect width="415" height="195" rx="6" fill="{BG}"/>
  <text x="25" y="32" fill="{TITLE}" font-size="16" font-weight="600" font-family="Segoe UI, Ubuntu, Sans-Serif">Pitchfork-and-Torch GitHub Stats</text>
  {"".join(items)}
</svg>
'''


def langs_svg(counts: list[tuple[str, int]]) -> str:
    total = sum(n for _, n in counts) or 1
    bars = []
    y = 58
    for name, n in counts[:8]:
        pct = n / total
        w = max(8, int(365 * pct))
        color = LANG_COLOR.get(name, ICON)
        label = f"{name} {pct * 100:.1f}%"
        bars.append(
            f'<text x="25" y="{y}" fill="{TEXT}" font-size="12" font-family="Segoe UI, Ubuntu, Sans-Serif">{html.escape(label)}</text>'
            f'<rect x="25" y="{y + 6}" width="365" height="8" rx="4" fill="#12131c"/>'
            f'<rect x="25" y="{y + 6}" width="{w}" height="8" rx="4" fill="{color}"/>'
        )
        y += 28
    height = max(195, y + 16)
    return f'''<svg width="415" height="{height}" viewBox="0 0 415 {height}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img">
  <title>Top languages</title>
  <rect width="415" height="{height}" rx="6" fill="{BG}"/>
  <text x="25" y="32" fill="{TITLE}" font-size="16" font-weight="600" font-family="Segoe UI, Ubuntu, Sans-Serif">Most Used Languages</text>
  {"".join(bars)}
</svg>
'''


def search_count(q: str) -> int:
    data = gh_json(["api", f"search/issues?q={q}&per_page=1"])
    return int(data.get("total_count") or 0)


def main() -> None:
    PINS.mkdir(parents=True, exist_ok=True)
    STATS.mkdir(parents=True, exist_ok=True)

    all_repos = gh_json(
        [
            "repo",
            "list",
            "Pitchfork-and-Torch",
            "--limit",
            "100",
            "--no-archived",
            "--source",
            "--json",
            "name,stargazerCount,forkCount,primaryLanguage,description,url",
        ]
    )
    by_name = {r["name"]: r for r in all_repos}

    for spec in FEATURED:
        meta = by_name.get(spec["repo"], {})
        lang = (meta.get("primaryLanguage") or {}).get("name") or "C"
        stars = int(meta.get("stargazerCount") or 0)
        forks = int(meta.get("forkCount") or 0)
        svg = pin_svg(spec["title"], spec["desc"], lang, stars, forks)
        path = PINS / f"{spec['repo']}.svg"
        path.write_text(svg, encoding="utf-8", newline="\n")
        print("pin", path.name, lang, stars)

    lang_counts: dict[str, int] = {}
    stars = 0
    for r in all_repos:
        stars += int(r.get("stargazerCount") or 0)
        lang = (r.get("primaryLanguage") or {}).get("name")
        if lang:
            lang_counts[lang] = lang_counts.get(lang, 0) + 1
    ranked = sorted(lang_counts.items(), key=lambda kv: kv[1], reverse=True)

    user = gh_json(["api", "users/Pitchfork-and-Torch"])
    prs = search_count("author:Pitchfork-and-Torch+type:pr")
    issues = search_count("author:Pitchfork-and-Torch+type:issue")

    (STATS / "stats.svg").write_text(
        stats_svg(
            stars=stars,
            prs=prs,
            issues=issues,
            repos=int(user.get("public_repos") or len(all_repos)),
            followers=int(user.get("followers") or 0),
        ),
        encoding="utf-8",
        newline="\n",
    )
    (STATS / "top-langs.svg").write_text(langs_svg(ranked), encoding="utf-8", newline="\n")
    print("stats stars", stars, "prs", prs, "issues", issues, "langs", [n for n, _ in ranked[:8]])


if __name__ == "__main__":
    main()
