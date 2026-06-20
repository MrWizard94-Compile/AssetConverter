#!/usr/bin/env python3
"""Repair animation .mcmeta width/height for already-upscaled PNGs."""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.paths import OUTPUT_ASSETS_DIR, SOURCES_DIR
from config.registry import texture_namespace
from pipeline.run_upscale import find_source_texture_roots
from pipeline.texture_policy import infer_image_scale, write_mcmeta_sidecar


def fix_namespace(mod_name: str) -> int:
    namespace = texture_namespace(mod_name)
    output_dir = os.path.join(OUTPUT_ASSETS_DIR, namespace, "textures")
    if not os.path.isdir(output_dir):
        print(f"[-] {mod_name}: no output textures")
        return 0

    source_roots = find_source_texture_roots(mod_name)
    if not source_roots:
        print(f"[-] {mod_name}: no source roots")
        return 0

    fixed = 0
    skipped = 0
    for root, _, files in os.walk(output_dir):
        for file in files:
            if not file.endswith(".png"):
                continue
            dest_png = os.path.join(root, file)
            rel_path = os.path.relpath(dest_png, output_dir)

            src_png = None
            for source_root in source_roots:
                candidate = os.path.join(source_root, rel_path)
                if os.path.isfile(candidate):
                    src_png = candidate
                    break
            if not src_png or not os.path.isfile(src_png + ".mcmeta"):
                continue

            scale = infer_image_scale(src_png, dest_png)
            if scale <= 1:
                continue

            try:
                if write_mcmeta_sidecar(src_png, dest_png, image_scale=scale):
                    fixed += 1
            except OSError:
                skipped += 1

    suffix = f", {skipped} skipped" if skipped else ""
    print(f"[+] {mod_name}: {fixed} animation mcmeta file(s) scaled{suffix}")
    return fixed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mod", nargs="?", help="Registry mod id. Omit for all output mods.")
    args = parser.parse_args()

    if args.mod:
        mods = [args.mod]
    else:
        mods = sorted(
            name
            for name in os.listdir(OUTPUT_ASSETS_DIR)
            if os.path.isdir(os.path.join(OUTPUT_ASSETS_DIR, name, "textures"))
        )

    total = 0
    for mod in mods:
        total += fix_namespace(mod)

    print(f"[*] Done. {total} mcmeta files repaired.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())