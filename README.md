# AssetConverter

Minecraft 1.20.1 Forge texture upscaling pipeline for the **Base-Wars** modpack. Clones mod source trees into the repo, upscales 16× pixel-art textures to 32× with xBRZ and size-aware policy, then builds and deploys the `Base-Wars_32x` resource pack to a CurseForge instance.

## Purpose

AssetConverter automates three jobs that would otherwise be manual and error-prone:

1. **Source acquisition** — clone public mod repos (or extract closed-source JARs) into `sources/` so textures are versioned in git, not scattered at the project root.
2. **Upscale** — apply per-texture strategy (xBRZ, nearest-neighbor, or copy-as-is) and write results to `output/assets/<namespace>/`.
3. **Pack + deploy** — assemble all upscaled namespaces into one resource pack and copy it into the Minecraft instance `resourcepacks/` folder.

The mod catalog, clone branches, and JAR fallbacks live in `config/registry.py`. Work queue and ATM10 gap analysis live in `docs/MOD_QUEUE.md`.

## Directory structure

```
AssetConverter/
├── SOUL.md                  # Engineering principles (Corwin)
├── ac.py                    # CLI entry point
├── mod_sources.py           # Shim re-exporting config.registry (legacy imports)
├── config/
│   ├── paths.py             # All paths; env overrides
│   └── registry.py          # MOD_REPOS, CLONE_BRANCHES, jar fallbacks
├── pipeline/                # Core pipeline modules
│   ├── pull_mod_sources.py  # Clone / extract → sources/
│   ├── run_upscale.py       # Upscale one namespace
│   ├── build_resourcepack.py# Package + deploy pack
│   ├── texture_policy.py    # Per-texture upscale strategy
│   └── audit_mod.py         # Pre-flight texture audit
├── scripts/                 # Git helpers, batch runners, ATM10 analysis
│   ├── git_commit_sources.py
│   └── _atm10_analyze.py    # Invoked by `ac.py status`
├── sources/                 # Mod source trees (committed to repo)
├── output/
│   ├── assets/              # Upscaled textures per namespace
│   └── resourcepack/        # Built pack (Base-Wars_32x/)
├── local/                   # Machine-local only (not committed)
│   ├── cache/               # Optional upscale cache
│   └── jars/                # Downloaded Modrinth / fallback JARs
├── data/                    # ATM10 research JSON
├── docs/
│   ├── WORKFLOW.md          # Step-by-step pipeline guide
│   └── MOD_QUEUE.md         # Upscale priority queue
├── references/              # External API / setup notes
└── tools/                   # Native binaries (xBRZ, waifu2x) — not in git
```

**What belongs in the repo vs locally**

| Path | In git? | Notes |
|------|---------|-------|
| `sources/` | Yes | Pulled mod trees; committed after every `pull` |
| `output/assets/` | Yes | Upscaled textures; commit after each mod |
| `output/resourcepack/` | Optional | Rebuilt by `build`; deploy copy is on the instance |
| `local/` | No | Cache and downloaded JARs |
| `tools/` | No | System / machine-specific binaries |

Sources **never** land at the project root. `ac.py pull` writes only under `sources/<mod>/`.

## CLI usage

All commands run from the repo root:

```powershell
cd C:\Users\Bulkl\OneDrive\Desktop\AssetConverter
```

### `pull` — clone sources and git commit

```powershell
# One mod
python ac.py pull oh_the_biomes_weve_gone

# Multiple mods
python ac.py pull create farmersdelight ae2
```

Runs `pipeline/pull_mod_sources.py` then `scripts/git_commit_sources.py`. Clones into `sources/<mod>/` using URLs and branches from `config/registry.py`. Closed-source Macaw's mods and sparse repos fall back to Modrinth JAR extraction (`MODRINTH_JAR_MODS`).

### `upscale` — process one namespace

```powershell
python ac.py upscale oh_the_biomes_weve_gone

# Alternate methods (default: xbrz)
python ac.py upscale create --method hq2x
python ac.py upscale botania --method waifu2x
```

Reads textures from `sources/`, writes to `output/assets/<namespace>/textures/`. Multi-root mods (Thermal, Mekanism, EnderIO) are merged automatically via `find_source_texture_roots()`.

### `build` — package and deploy resource pack

```powershell
python ac.py build
```

1. Copies every namespace under `output/assets/` into `output/resourcepack/Base-Wars_32x/assets/`
2. Writes `pack.mcmeta` (format 15 — Minecraft 1.20.1)
3. Deploys the pack to the instance `resourcepacks/` folder (see **Deployment** below)

### `status` — mod queue / gap analysis

```powershell
python ac.py status
```

Re-runs ATM10 mod-list analysis (`scripts/_atm10_analyze.py`) against `output/assets/` and `config/registry.py`. Use this to refresh `docs/MOD_QUEUE.md` priorities.

## Workflow (summary)

Full step-by-step guide: `docs/WORKFLOW.md`.

```
pick mod from docs/MOD_QUEUE.md
    → add to config/registry.py (if new)
    → python ac.py pull <mod>      # sources/ + auto git commit
    → python ac.py upscale <mod>   # output/assets/<mod>/
    → git add output/assets/<mod> && git commit
    → python ac.py build           # deploy to instance
```

## Deployment path

Defined in `config/paths.py`:

| Setting | Default |
|---------|---------|
| Instance | `C:\Users\Bulkl\curseforge\minecraft\Instances\Base-Wars_Stripped` |
| Deploy target | `<instance>/resourcepacks/Base-Wars_32x/` |
| Pack name | `Base-Wars_32x` |

Override on other machines:

```powershell
$env:ASSETCONVERTER_INSTANCE = "D:\Games\minecraft\Instances\MyInstance"
$env:ASSETCONVERTER_ROOT     = "D:\dev\AssetConverter"
```

`build` removes any existing `Base-Wars_32x` folder in `resourcepacks/` and copies the freshly built pack. Enable the pack in-game under Options → Resource Packs.

## Environment overrides

| Variable | Default | Purpose |
|----------|---------|---------|
| `ASSETCONVERTER_ROOT` | Repo root (parent of `config/`) | Relocate entire project |
| `ASSETCONVERTER_INSTANCE` | CurseForge `Base-Wars_Stripped` path | Deploy target instance |

## Configuration reference

- **`config/registry.py`** — `MOD_REPOS` (clone URLs), `CLONE_BRANCHES` (1.20.1 tags), `JAR_ONLY_MODS`, `JAR_FALLBACK_MODS`, `MODRINTH_JAR_MODS`, `SKIP_MODS`. Add new mods here before pulling.
- **`config/paths.py`** — `SOURCES_DIR`, `OUTPUT_ASSETS_DIR`, `RESOURCEPACK_DIR`, `DEPLOY_DIR`, `PACK_FORMAT`.
- **`docs/MOD_QUEUE.md`** — 83 mods done; prioritized list of ATM10 candidates still to add.

## Status

- **83** namespaces upscaled (65,500+ textures) — see `docs/MOD_QUEUE.md`
- Next target: `oh_the_biomes_weve_gone` (~2,200 PNGs)

## Further reading

- `docs/WORKFLOW.md` — pull → upscale → build → deploy, git flow, mod queue process
- `docs/MOD_QUEUE.md` — ATM10 priority table and registry gaps
- `references/pipeline-architecture.md` — module map and data flow
- `SOUL.md` — project engineering standards