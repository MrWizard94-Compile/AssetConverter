#!/usr/bin/env python3
"""AssetConverter CLI — pull sources to repo, upscale, build pack."""
import argparse
import os
import subprocess
import sys

from config.paths import PROJECT_ROOT


def run(script, *args):
    path = None

    candidates = [
        os.path.join(PROJECT_ROOT, "pipeline", script),
        os.path.join(PROJECT_ROOT, "scripts", script),
    ]
    for candidate in candidates:
        if os.path.isfile(candidate):
            path = candidate
            break
    if not path:
        print(f"[-] Script not found: {script}")
        sys.exit(1)
    result = subprocess.run([sys.executable, path, *args], cwd=PROJECT_ROOT)
    sys.exit(result.returncode)


def main():
    parser = argparse.ArgumentParser(description="AssetConverter")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_pull = sub.add_parser("pull", help="Clone mod sources into sources/ and git commit")
    p_pull.add_argument("mods", nargs="+", help="Mod IDs")

    p_up = sub.add_parser("upscale", help="Upscale mod textures")
    p_up.add_argument("mod", help="Mod namespace")
    p_up.add_argument("--method", default="xbrz", choices=["xbrz", "hq2x", "waifu2x"])

    sub.add_parser("build", help="Build and deploy resource pack")
    sub.add_parser("status", help="Show mod queue status")

    args = parser.parse_args()
    if args.cmd == "pull":
        run("pull_mod_sources.py", *args.mods)
        run("git_commit_sources.py", *args.mods)
    elif args.cmd == "upscale":
        run("run_upscale.py", args.mod, "--method", args.method)
    elif args.cmd == "build":
        run("build_resourcepack.py")
    elif args.cmd == "status":
        run("_atm10_analyze.py")


if __name__ == "__main__":
    main()