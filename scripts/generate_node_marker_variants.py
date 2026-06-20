#!/usr/bin/env python3
"""Generate per-NodeType node_marker block textures from the base pedestal design."""
from __future__ import annotations

import os
from pathlib import Path

from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = (
    PROJECT_ROOT
    / "sources"
    / "nodecore"
    / "src"
    / "main"
    / "resources"
    / "assets"
    / "nodecore"
    / "textures"
    / "block"
)

BASE_TEXTURE = SOURCE_DIR / "node_marker.png"

# Original purple glow tiers in the base texture.
GLOW_MAP = {
    (65, 28, 95, 255): "dark",
    (105, 48, 155, 255): "medium",
    (145, 75, 210, 255): "bright",
}

# Steampunk industrial accent palettes per NodeType.
TYPE_PALETTES: dict[str, dict[str, tuple[int, int, int]]] = {
    "ore_iron": {
        "dark": (55, 58, 62),
        "medium": (130, 135, 145),
        "bright": (210, 215, 225),
    },
    "ore_copper": {
        "dark": (100, 45, 22),
        "medium": (175, 85, 38),
        "bright": (235, 125, 55),
    },
    "ore_brass": {
        "dark": (110, 82, 28),
        "medium": (175, 135, 48),
        "bright": (235, 195, 75),
    },
    "ore_quartz": {
        "dark": (45, 75, 85),
        "medium": (100, 165, 190),
        "bright": (200, 240, 255),
    },
    "lush_hydro": {
        "dark": (22, 70, 62),
        "medium": (38, 130, 108),
        "bright": (72, 200, 170),
    },
    "quartz_rift": {
        "dark": (95, 22, 18),
        "medium": (155, 40, 28),
        "bright": (225, 65, 42),
    },
}


def recolor_glow(base: Image.Image, palette: dict[str, tuple[int, int, int]]) -> Image.Image:
    out = base.copy()
    pixels = out.load()
    width, height = out.size

    for y in range(height):
        for x in range(width):
            rgba = pixels[x, y]
            tier = GLOW_MAP.get(rgba)
            if tier is None:
                continue
            r, g, b = palette[tier]
            pixels[x, y] = (r, g, b, rgba[3])

    return out


def main() -> None:
    if not BASE_TEXTURE.is_file():
        raise SystemExit(f"Base texture not found: {BASE_TEXTURE}")

    base = Image.open(BASE_TEXTURE).convert("RGBA")
    if base.size != (16, 16):
        raise SystemExit(f"Expected 16x16 base texture, got {base.size}")

    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    for node_type, palette in TYPE_PALETTES.items():
        variant = recolor_glow(base, palette)
        out_path = SOURCE_DIR / f"node_marker_{node_type}.png"
        variant.save(out_path, format="PNG")
        written.append(out_path)
        print(f"[+] {out_path.name} ({node_type})")

    print(f"[*] Wrote {len(written)} variants to {SOURCE_DIR}")


if __name__ == "__main__":
    main()