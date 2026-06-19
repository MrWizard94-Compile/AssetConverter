# Pipeline Architecture

## Data flow

```
MOD_REPOS (config/registry.py)
        ↓ pull_mod_sources.py
   sources/<mod>/assets/<namespace>/textures/
        ↓ run_upscale.py (xBRZ + texture_policy)
   output/assets/<namespace>/textures/
        ↓ build_resourcepack.py
   output/resourcepack/Base-Wars_32x/
        ↓ deploy
   CurseForge instance resourcepacks/
```

## Key modules

| Module | Role |
|--------|------|
| `config/paths.py` | Central paths; env overrides |
| `config/registry.py` | Mod catalog, branches, jar fallbacks |
| `pipeline/run_upscale.py` | Multi-root discovery + upscale |
| `pipeline/pull_mod_sources.py` | Git clone + Modrinth jar |
| `pipeline/texture_policy.py` | Per-texture strategy |
| `pipeline/build_resourcepack.py` | Pack assembly + deploy |

## Multi-root sources

`find_source_texture_roots()` walks `sources/` for all `assets/<namespace>/textures` trees. Used by:

- Thermal (4 CoFH repos → 1 `thermal` namespace)
- Mekanism (generators/tools submodules)
- EnderIO (armory/conduits/core/machines)
- Aether (builtin resource packs)