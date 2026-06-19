"""Mod queue — discover pending work for the autonomous engine."""
import os
import re

from config.paths import OUTPUT_ASSETS_DIR
from config.registry import MOD_REPOS, texture_namespace

# Priority order (registry mod_id). Sync with docs/MOD_QUEUE.md top section.
QUEUE_PRIORITY = [
    "relics_mod",
    "modern_industrialization",
    "storage_delight",
    "iron_furnaces",
    "rftools_utility",
    "integrated_terminals",
    "rftools_base",
    "reliquified_artifacts",
    "extrastorage",
    "ars_energistique",
    "rftools_storage",
    "wireless_chargers",
    "functional_storage",
    "creeper_overhaul",
    "modularrouters",
    "sereneseasons",
    "yungs_better_mineshafts",
    "yungs_better_dungeons",
    "yungs_better_strongholds",
    "simple_magnets",
    "yungs_better_ocean_monuments",
    "yungs_better_nether_fortresses",
    "mo_structures",
    "yungs_extras",
    "yungs_better_desert_temples",
]


def _has_upscaled_assets(namespace):
    tex_dir = os.path.join(OUTPUT_ASSETS_DIR, namespace, "textures")
    if not os.path.isdir(tex_dir):
        return False
    return any(
        file.endswith(".png")
        for _, _, files in os.walk(tex_dir)
        for file in files
    )


def is_complete(mod_id):
    return _has_upscaled_assets(texture_namespace(mod_id))


def discover_pending():
    """All registry mods without upscaled output (beyond explicit queue)."""
    out = []
    for mod_id in sorted(MOD_REPOS):
        if mod_id in QUEUE_PRIORITY:
            continue
        if not is_complete(mod_id):
            out.append(mod_id)
    return out


def pending_mods():
    out = []
    for mod_id in QUEUE_PRIORITY:
        if mod_id not in MOD_REPOS:
            continue
        if not is_complete(mod_id):
            out.append(mod_id)
    if not out:
        out = discover_pending()
    return out


def next_mod():
    pending = pending_mods()
    return pending[0] if pending else None


def queue_status():
    done = []
    pending = []
    for mod_id in QUEUE_PRIORITY:
        if mod_id not in MOD_REPOS:
            pending.append((mod_id, "not_in_registry"))
        elif is_complete(mod_id):
            done.append(mod_id)
        else:
            pending.append((mod_id, "ready"))
    return done, pending


def parse_done_from_mod_queue(path):
    """Read DONE mod_ids from docs/MOD_QUEUE.md table rows."""
    if not os.path.isfile(path):
        return set()
    done = set()
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if "**DONE**" not in line:
                continue
            match = re.search(r"`([a-z0-9_]+)`", line)
            if match:
                done.add(match.group(1))
    return done