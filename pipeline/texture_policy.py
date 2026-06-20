"""Size-aware upscale strategy and Minecraft texture sidecar handling."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
import os
import shutil
from enum import Enum

from PIL import Image

SCALE = 2

# GUI mods: nearest-neighbor only (layout-sensitive sprites).
UI_MODS = {"jei", "emi", "rei"}


class Strategy(str, Enum):
    PIXEL_ART = "pixel_art"
    NEAREST = "nearest"
    COPY = "copy"


def classify_texture(width: int, height: int, mod_name: str = "") -> Strategy:
    if mod_name in UI_MODS:
        return Strategy.NEAREST

    if width == 16 and height == 16:
        return Strategy.PIXEL_ART

    if width == 32 and height == 32:
        return Strategy.COPY

    short_side = min(width, height)
    long_side = max(width, height)

    if short_side >= 32 and long_side <= 64:
        return Strategy.COPY

    if long_side >= short_side * 4:
        return Strategy.NEAREST

    if short_side <= 16:
        return Strategy.PIXEL_ART

    return Strategy.NEAREST


def nearest_scale(image: Image.Image, scale: int = SCALE) -> Image.Image:
    image = image.convert("RGBA")
    return image.resize((image.width * scale, image.height * scale), Image.NEAREST)


def copy_image(src_path: str, dest_path: str) -> None:
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    shutil.copy2(src_path, dest_path)


def _scale_animation_meta(animation: dict, scale: int) -> None:
    if scale <= 1:
        return
    for key in ("width", "height"):
        value = animation.get(key)
        if isinstance(value, (int, float)) and value > 0:
            animation[key] = int(value * scale)


def write_mcmeta_sidecar(src_png: str, dest_png: str, image_scale: int = 1) -> bool:
    """Write .png.mcmeta; scale animation width/height when image_scale > 1."""
    src_meta = src_png + ".mcmeta"
    if not os.path.isfile(src_meta):
        return False

    dest_meta = dest_png + ".mcmeta"
    os.makedirs(os.path.dirname(dest_meta), exist_ok=True)

    with open(src_meta, encoding="utf-8") as handle:
        raw = handle.read()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        cleaned = []
        for line in raw.splitlines():
            if "//" in line:
                line = line.split("//", 1)[0].rstrip()
            cleaned.append(line)
        try:
            data = json.loads("\n".join(cleaned))
        except json.JSONDecodeError:
            shutil.copy2(src_meta, dest_meta)
            return True

    animation = data.get("animation")
    if animation and image_scale > 1:
        _scale_animation_meta(animation, image_scale)

    with open(dest_meta, "w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2)
        handle.write("\n")
    return True


def copy_sidecar(src_png: str, dest_png: str) -> bool:
    return write_mcmeta_sidecar(src_png, dest_png, image_scale=1)


def infer_image_scale(src_png: str, dest_png: str) -> int:
    """Return width ratio dest/src when both exist and src width > 0."""
    if not os.path.isfile(src_png) or not os.path.isfile(dest_png):
        return 1
    try:
        with Image.open(src_png) as src_image, Image.open(dest_png) as dest_image:
            if src_image.width <= 0:
                return 1
            ratio = dest_image.width / src_image.width
            if abs(ratio - round(ratio)) < 0.01 and ratio >= 1:
                return int(round(ratio))
    except OSError:
        return 1
    return 1