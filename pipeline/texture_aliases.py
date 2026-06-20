"""Synthetic texture paths required by models but absent from mod source trees."""
from __future__ import annotations

import os
import shutil

# dest relative to textures/ -> source relative to textures/
ALIASES: dict[str, dict[str, str]] = {
    "vs_clockwork": {
        "block/duct_tank.png": "block/duct_tank_connected.png",
        "block/duct_tank_top.png": "block/duct_tank_top_connected.png",
    },
}


def apply_aliases(namespace: str, textures_dir: str) -> int:
    mapping = ALIASES.get(namespace)
    if not mapping:
        return 0

    created = 0
    for dest_rel, src_rel in mapping.items():
        dest_path = os.path.join(textures_dir, dest_rel.replace("/", os.sep))
        if os.path.isfile(dest_path):
            continue
        src_path = os.path.join(textures_dir, src_rel.replace("/", os.sep))
        if not os.path.isfile(src_path):
            continue
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy2(src_path, dest_path)
        src_meta = src_path + ".mcmeta"
        dest_meta = dest_path + ".mcmeta"
        if os.path.isfile(src_meta) and not os.path.isfile(dest_meta):
            shutil.copy2(src_meta, dest_meta)
        created += 1
    return created


def apply_all_aliases(output_assets_dir: str) -> int:
    total = 0
    if not os.path.isdir(output_assets_dir):
        return 0
    for namespace in ALIASES:
        textures_dir = os.path.join(output_assets_dir, namespace, "textures")
        if os.path.isdir(textures_dir):
            count = apply_aliases(namespace, textures_dir)
            if count:
                print(f"[+] {namespace}: {count} texture alias(es) applied")
            total += count
    return total