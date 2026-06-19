# Workflow

Step-by-step guide for pulling mod sources, upscaling textures, building the resource pack, and deploying to the Base-Wars CurseForge instance.

## Principles (SOUL.md)

- **Sources live in the repo** under `sources/` — never at the project root or outside git.
- **Pull commits immediately** — `ac.py pull` runs `git_commit_sources.py` after every clone/extract.
- **Upscale output is committed separately** — `output/assets/<namespace>/` is staged and committed by hand after each mod.
- **Local-only paths** — `local/cache`, `local/jars`, and `tools/` stay off git; only `sources/` and `output/assets/` are versioned artifacts.
- **Registry is the source of truth** — every pullable mod must exist in `config/registry.py` before `ac.py pull` will succeed.

## Pipeline overview

```
docs/MOD_QUEUE.md          config/registry.py
        │                           │
        └──────── pick mod ─────────┘
                    │
                    ▼
         python ac.py pull <mod>
                    │
         sources/<mod>/  ──git commit──►  repo
                    │
                    ▼
         python ac.py upscale <mod>
                    │
         output/assets/<mod>/  ──git commit──►  repo
                    │
                    ▼
         python ac.py build
                    │
         output/resourcepack/Base-Wars_32x/
                    │
                    ▼
         <instance>/resourcepacks/Base-Wars_32x/   (in-game)
```

---

## Step 1 — Pick a mod from the queue

Open `docs/MOD_QUEUE.md`. The **Top 15** table lists ATM10 mods ranked by estimated PNG count, CurseForge popularity, and content weight.

Before pulling, confirm:

1. The `mod_id` is not already listed under **Upscaled namespaces** in `MOD_QUEUE.md`.
2. The mod has a public repo (or is a known JAR-only / Modrinth entry).

If the mod is **not** in `config/registry.py` `MOD_REPOS`, add it first (see Step 2).

Refresh the queue after large batch upscales:

```powershell
python ac.py status
```

This re-runs `scripts/_atm10_analyze.py` and prints gaps between ATM10, `output/assets/`, and `MOD_REPOS`.

---

## Step 2 — Register the mod (new mods only)

Edit `config/registry.py`:

```python
MOD_REPOS = {
    # ...
    "oh_the_biomes_weve_gone": "https://github.com/Potion-Studios/Oh-The-Biomes-Weve-Gone.git",
}

CLONE_BRANCHES = {
    # only if not default branch
    "oh_the_biomes_weve_gone": "main",
}
```

Registry sections and when to use them:

| Section | Use case |
|---------|----------|
| `MOD_REPOS` | Git clone URL for every pullable mod |
| `CLONE_BRANCHES` | Non-default branch (target **1.20.1 / 1.20.x Forge**) |
| `JAR_ONLY_MODS` | No public source; extract textures from a named JAR |
| `JAR_FALLBACK_MODS` | Repo exists but JAR has more textures — pick richer source |
| `MODRINTH_JAR_MODS` | Closed-source Macaw's mods — download from Modrinth CDN |
| `SKIP_MODS` | Libraries / performance mods with no useful textures |

Jar paths resolve from `local/jars/` first, then the instance `mods/` folder (`config/paths.py` → `MODS_DIR`).

Optional preflight after registration:

```powershell
python pipeline/audit_mod.py <mod_id>
```

Reports PNG counts, size distribution, and predicted upscale strategy per `texture_policy.py`.

---

## Step 3 — Pull sources

```powershell
python ac.py pull <mod_id>

# Examples
python ac.py pull oh_the_biomes_weve_gone
python ac.py pull create farmersdelight
python ac.py pull thermal          # pulls 4 CoFH repos, reports merged texture count
```

### What `pull` does

1. **`pipeline/pull_mod_sources.py`**
   - Looks up `mod_id` in `config/registry.py` `MOD_REPOS`.
   - Shallow-clones (`git clone --depth 1`) into `sources/<mod>/` using `CLONE_BRANCHES` when set.
   - Skips re-clone if textures already exist at the expected path.
   - For `MODRINTH_JAR_MODS`, downloads the JAR to `local/jars/` and extracts `assets/<mod>/textures/` into a standard Gradle layout under `sources/<mod>/src/main/resources/`.
   - For monorepo namespaces (`mekanismgenerators`, `mekanismtools`), clones the host repo (`mekanism`) once.

2. **`scripts/git_commit_sources.py`**
   - `git add sources/<mod>/` (or host folder for monorepos)
   - `git commit -m "pull: <mod_id>"`
   - Prints `[=] No changes to commit` if the tree is unchanged.

### Expected source layout

Textures are discovered under paths matching:

```
sources/<repo>/.../assets/<namespace>/textures/**/*.png
```

Multi-root mods merge at upscale time:

| Namespace | Source roots |
|-----------|--------------|
| `thermal` | `thermal_core`, `thermal_foundation`, `thermal_expansion`, `thermal_innovation` |
| `mekanismgenerators` / `mekanismtools` | `sources/mekanism/` (monorepo) |
| `enderio` | Multiple `assets/enderio/textures` trees inside one clone |

### Pull failure checklist

- `mod_id` missing from `MOD_REPOS` → add to `config/registry.py`.
- Clone succeeded but 0 PNGs → wrong branch; update `CLONE_BRANCHES` or try `MODRINTH_JAR_MODS` / `JAR_FALLBACK_MODS`.
- Closed-source mod → add JAR name to `JAR_ONLY_MODS` and place JAR in instance `mods/` or `local/jars/`.

---

## Step 4 — Upscale

```powershell
python ac.py upscale <mod_id>

# Default: xBRZ 2×
python ac.py upscale oh_the_biomes_weve_gone

# Alternatives
python ac.py upscale create --method hq2x
python ac.py upscale botania --method waifu2x
```

### What `upscale` does

`pipeline/run_upscale.py`:

1. Discovers all texture roots via `find_source_texture_roots()`.
2. Classifies each PNG with `texture_policy.classify_texture()`.
3. Writes output to `output/assets/<namespace>/textures/`, preserving relative paths.
4. Copies `.png.mcmeta` sidecars alongside their PNGs.

### Upscale policy (`pipeline/texture_policy.py`)

| Condition | Strategy | Result |
|-----------|----------|--------|
| 16×16 | Pixel art | xBRZ / hq2x / waifu2x 2× |
| 32×32 | Copy | No resize |
| Short side ≥ 32, long ≤ 64 | Copy | Already pack-ready |
| Strip / odd aspect (long ≥ 4× short) | Nearest | 2× nearest-neighbor |
| JEI / EMI / REI (`UI_MODS`) | Nearest | Layout-sensitive UI sprites |

Default CLI method is **xbrz** — best for Minecraft pixel art. Use `hq2x` or `waifu2x` only when comparing quality on a specific mod.

### Git commit (upscale output)

Pull auto-commits sources; upscale does **not**. Commit assets after verifying output:

```powershell
git add output/assets/<mod_id>
git commit -m "upscale: <mod_id>"
```

For multi-namespace pulls (e.g. `thermal` writes one `thermal` folder), commit that namespace path.

---

## Step 5 — Build and deploy

```powershell
python ac.py build
```

### What `build` does

`pipeline/build_resourcepack.py`:

1. **Build** — Creates `output/resourcepack/Base-Wars_32x/`:
   - `assets/<namespace>/textures/` for every folder in `output/assets/`
   - `pack.mcmeta` with `pack_format: 15` (Minecraft 1.20.1)
2. **Deploy** — Copies the entire pack to:

   ```
   <ASSETCONVERTER_INSTANCE>/resourcepacks/Base-Wars_32x/
   ```

   Default instance (`config/paths.py`):

   ```
   C:\Users\Bulkl\curseforge\minecraft\Instances\Base-Wars_Stripped\resourcepacks\Base-Wars_32x\
   ```

3. Prints texture and sidecar counts per namespace.

Rebuild after **any** new upscale — `build` always packages **all** namespaces under `output/assets/`, not just the last mod.

### In-game verification

1. Launch the Base-Wars instance in CurseForge.
2. Options → Resource Packs → enable **Base-Wars_32x** (top of active list).
3. Spot-check blocks/items from the mod you just upscaled.

---

## Git commit flow (complete)

Two commit points per mod. Keep messages consistent for history grep.

| Stage | Command | Git action | Message pattern |
|-------|---------|------------|-----------------|
| Pull | `python ac.py pull <mod>` | Automatic | `pull: <mod>` |
| Upscale | `python ac.py upscale <mod>` | Manual | `upscale: <mod>` |
| Build | `python ac.py build` | None (deploy is local) | — |

### Single-mod example

```powershell
# 1. Register in config/registry.py (if new)

# 2. Pull + auto-commit sources
python ac.py pull oh_the_biomes_weve_gone

# 3. Upscale
python ac.py upscale oh_the_biomes_weve_gone

# 4. Commit upscaled assets
git add output/assets/oh_the_biomes_weve_gone
git commit -m "upscale: oh_the_biomes_weve_gone"

# 5. Rebuild pack and deploy
python ac.py build
```

### Batch example (queue top 3)

```powershell
python ac.py pull oh_the_biomes_weve_gone railcraft_reborn eternal_starlight

python ac.py upscale oh_the_biomes_weve_gone
git add output/assets/oh_the_biomes_weve_gone
git commit -m "upscale: oh_the_biomes_weve_gone"

python ac.py upscale railcraft_reborn
git add output/assets/railcraft_reborn
git commit -m "upscale: railcraft_reborn"

python ac.py upscale eternal_starlight
git add output/assets/eternal_starlight
git commit -m "upscale: eternal_starlight"

python ac.py build
```

---

## Mod queue process

`docs/MOD_QUEUE.md` is the working backlog. Maintain it in this loop:

### 1. Analyze

```powershell
python ac.py status
```

Cross-references:

- `data/atm10_mods_raw.json` — full ATM10 mod list
- `output/assets/` — what's already upscaled (83 namespaces)
- `config/registry.py` `MOD_REPOS` — what's registered for pull

### 2. Prioritize

`MOD_QUEUE.md` ranks candidates by:

- Estimated PNG count (texture surface area)
- CurseForge download count (player exposure)
- Content weight (tech / magic / decoration mods over libraries)

Mods in `SKIP_MODS` or without textures are excluded.

### 3. Register gaps

Top queue entries not yet in `MOD_REPOS` are listed at the bottom of `MOD_QUEUE.md` under **Add to registry**. Copy each into `config/registry.py` before pulling.

### 4. Process

For each mod, run Steps 3–5 above. Mark done informally by the namespace appearing in `MOD_QUEUE.md` **Upscaled namespaces** list (regenerate with `ac.py status` after batches).

### 5. Handle edge cases

| Situation | Action |
|-----------|--------|
| ATM10 slug ≠ mod_id (e.g. `the_twilight_forest` → `twilightforest`) | Use `mod_id` / namespace from `MOD_REPOS`, not CurseForge slug |
| Mod already upscaled under different folder name | Check **Upscaled namespaces** in `MOD_QUEUE.md` |
| 1.21 NeoForge ATM10 vs 1.20.1 Forge clone | Branches in `CLONE_BRANCHES` target 1.20.1; textures are usually compatible |
| Macaw's / closed-source | Already in `MODRINTH_JAR_MODS`; pull extracts from JAR |
| Sparse GitHub repo | Add `JAR_FALLBACK_MODS` entry with instance JAR filename |

---

## CLI reference

| Command | Script(s) | Input | Output |
|---------|-----------|-------|--------|
| `python ac.py pull <mods...>` | `pull_mod_sources.py`, `git_commit_sources.py` | `config/registry.py` | `sources/<mod>/` + git commit |
| `python ac.py upscale <mod> [--method xbrz\|hq2x\|waifu2x]` | `run_upscale.py` | `sources/` | `output/assets/<mod>/` |
| `python ac.py build` | `build_resourcepack.py` | `output/assets/` | `output/resourcepack/Base-Wars_32x/` + instance deploy |
| `python ac.py status` | `_atm10_analyze.py` | `data/`, `output/assets/`, registry | Console gap report |

---

## Adding a new mod (checklist)

- [ ] Mod listed or prioritized in `docs/MOD_QUEUE.md`
- [ ] `mod_id` + repo URL added to `config/registry.py` `MOD_REPOS`
- [ ] Branch added to `CLONE_BRANCHES` if not default
- [ ] JAR fallback configured if repo is sparse or closed-source
- [ ] `python ac.py pull <mod_id>` — sources committed
- [ ] `python pipeline/audit_mod.py <mod_id>` — optional preflight
- [ ] `python ac.py upscale <mod_id>` — assets written
- [ ] `git add output/assets/<mod_id> && git commit -m "upscale: <mod_id>"`
- [ ] `python ac.py build` — pack deployed to instance
- [ ] In-game visual check
- [ ] `python ac.py status` — refresh queue doc if processing a batch

---

## Related docs

- `docs/MOD_QUEUE.md` — ATM10 priority queue and registry gaps
- `config/registry.py` — mod catalog (URLs, branches, JAR maps)
- `config/paths.py` — paths and deployment target
- `references/pipeline-architecture.md` — module-level data flow
- `references/github-private-repo.md` — making the GitHub repo private