#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


REPO = "4riful/xetta-web-appsec-field-manual"
OUT = Path("assets/star-history.png")
WIDTH = 1000
HEIGHT = 540


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    names = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def fetch_stars() -> list[datetime]:
    stars: list[datetime] = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{REPO}/stargazers?per_page=100&page={page}"
        req = urllib.request.Request(
            url,
            headers={
                "Accept": "application/vnd.github.star+json",
                "User-Agent": "xetta-star-history-png",
            },
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.load(resp)
        if not data:
            break
        for item in data:
            value = item.get("starred_at")
            if value:
                stars.append(datetime.fromisoformat(value.replace("Z", "+00:00")))
        if len(data) < 100:
            break
        page += 1
    return sorted(stars)


def draw() -> None:
    stars = fetch_stars()
    now = datetime.now(timezone.utc)
    start = min(stars) if stars else now
    end = max(now, max(stars) if stars else now)
    if (end - start).total_seconds() < 86400:
        end = start + timedelta(days=1)

    bg = "#0d1117"
    panel = "#161b22"
    grid = "#30363d"
    text = "#c9d1d9"
    muted = "#8b949e"
    accent = "#facc15"
    accent2 = "#7c3aed"

    img = Image.new("RGB", (WIDTH, HEIGHT), bg)
    d = ImageDraw.Draw(img)
    title = load_font(32, True)
    label = load_font(18)
    small = load_font(14)

    left, top, right, bottom = 86, 116, WIDTH - 56, HEIGHT - 86
    d.rounded_rectangle((32, 32, WIDTH - 32, HEIGHT - 32), radius=24, fill=panel, outline=grid, width=2)
    d.text((64, 54), "Star History", fill=text, font=title)
    d.text((64, 92), REPO, fill=muted, font=label)
    d.text((WIDTH - 220, 62), f"{len(stars)} GitHub Stars", fill=accent, font=label)

    max_y = max(1, len(stars))
    max_tick = max(1, math.ceil(max_y / 5) * 5 if max_y > 5 else max_y)
    span = max(1.0, (end - start).total_seconds())

    for i in range(6):
        y = bottom - (bottom - top) * i / 5
        d.line((left, y, right, y), fill=grid, width=1)
        val = round(max_tick * i / 5)
        d.text((30, y - 9), str(val), fill=muted, font=small)

    d.line((left, top, left, bottom), fill=grid, width=2)
    d.line((left, bottom, right, bottom), fill=grid, width=2)

    points: list[tuple[float, float]] = []
    for idx, ts in enumerate(stars, 1):
        x = left + (right - left) * (ts - start).total_seconds() / span
        y = bottom - (bottom - top) * idx / max_tick
        points.append((x, y))

    if points:
        base = (left, bottom)
        d.line([base, *points], fill=accent, width=4, joint="curve")
        for x, y in points:
            d.ellipse((x - 6, y - 6, x + 6, y + 6), fill=accent, outline="#fff8c5", width=2)
    else:
        d.text((left + 240, top + 120), "No stars yet", fill=muted, font=title)

    start_label = start.strftime("%b %d, %Y")
    end_label = end.strftime("%b %d, %Y")
    d.text((left, bottom + 22), start_label, fill=muted, font=small)
    w = d.textlength(end_label, font=small)
    d.text((right - w, bottom + 22), end_label, fill=muted, font=small)
    d.text((left, HEIGHT - 58), "Generated from GitHub stargazer timestamps. Click to open star-history.com.", fill=muted, font=small)
    d.rectangle((WIDTH - 276, HEIGHT - 64, WIDTH - 64, HEIGHT - 40), fill=accent2)
    d.text((WIDTH - 260, HEIGHT - 61), "star-history compatible", fill="#ffffff", font=small)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)


if __name__ == "__main__":
    try:
        draw()
    except Exception as exc:
        print(f"failed to generate {OUT}: {exc}", file=sys.stderr)
        raise
