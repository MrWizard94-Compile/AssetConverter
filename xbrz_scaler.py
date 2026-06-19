"""xBRZ 2x upscaler for Minecraft RGBA textures."""

from __future__ import annotations

from PIL import Image

from xbrz_lib import scale_pillow

SCALE = 2


def upscale_rgba(image: Image.Image) -> Image.Image:
    image = image.convert("RGBA")
    return scale_pillow(image, SCALE)