# MOD_QUEUE — ATM10 Upscale Priority

> Generated 2026-06-19 from `data/atm10_mods_raw.json` cross-referenced with `output/assets/` and `config/registry.py` `MOD_REPOS`.

## Upscaled namespaces (`output/assets/`)

**84** namespaces already processed:

```
actuallyadditions, ae2, aether, biomeswevegone, alexscaves, another_furniture, apotheosis, aquaculture, ars_nouveau, artifacts, bellsandwhistles, biomesoplenty, botania, brewinandchewin, chipped, comforts, cookingforblockheads, copycats, create, create_central_kitchen, create_connected, create_enchantment_industry, create_hypertube, create_jetpack, create_new_age, create_sa, createaddition, createbigcannons, createdeco, createendertransmission, createoreexcavation, deeperdarker, draconicevolution, enderio, evilcraft, farmersdelight, fluxnetworks, forbidden_arcanus, handcrafted, iceandfire, immersiveengineering, industrialforegoing, integrateddynamics, interiors, ironjetpacks, irons_spellbooks, jei, mcwbridges, mcwdoors, mcwfences, mcwlights, mcwroofs, mcwwindows, mekanism, mekanismgenerators, mekanismtools, minecolonies, mowziesmobs, mysticalagradditions, mysticalagriculture, occultism, pneumaticcraft, powah, productivebees, quark, railways, rechiseled, refinedstorage, reliquary, securitycraft, sliceanddice, sophisticatedbackpacks, sophisticatedstorage, storagedrawers, supplementaries, tconstruct, thermal, trackwork, trashcans, twilightforest, valkyrienskies, vs_clockwork, waystones, xnet
```

## Summary

| Metric | Value |
|--------|------:|
| ATM10 mods in research JSON | 477 |
| Already upscaled (namespace match) | 84 |
| ATM10 mods matched to upscaled set | 60 |
| Remaining candidates (public GitHub/GitLab) | 170 |
| `MOD_REPOS` entries | 98 |

## Top 15 — Next mods to upscale

Prioritized by **estimated PNG count** + **CurseForge popularity** + content weight (tech/magic/decoration).
Excludes libraries, QoL-only mods, and namespaces already present in `output/assets/`.

| Priority | mod_id | repo_url | branch | est_png_count | curseforge_popularity note |
|---------:|--------|----------|--------|--------------:|----------------------------|
| 1 | `oh_the_biomes_weve_gone` **DONE** | https://github.com/Potion-Studios/Oh-The-Biomes-Weve-Gone.git | `main` | 1114 | **DONE** — namespace `biomeswevegone`, 1114 PNG upscaled |
| 2 | `railcraft_reborn` | https://github.com/railcraft-reborn/railcraft.git | `main` | 950 | 18M CF; classic tech/rail mod reboot with huge item/block set |
| 3 | `eternal_starlight` | https://github.com/LeoMinecraftModding/eternal-starlight.git | `main` | 750 | New ATM10 dimension mod; high texture surface area |
| 4 | `the_undergarden` | https://github.com/quek04/The-Undergarden.git | `main` | 680 | 48M CF; full dimension with mobs, gear, and biomes |
| 5 | `productivetrees` | https://github.com/JDKDigital/productivetrees.git | `main` | 520 | 20M CF; pairs with Productive Bees already upscaled |
| 6 | `extreme_reactors` | https://github.com/ZeroNoRyouki/ExtremeReactors2.git | `main` | 420 | Big Reactors successor; 94M CF, reactor GUI + multiblock parts |
| 7 | `relics_mod` | https://github.com/SSKirillSS/relics.git | `main` | 280 | 57M CF; popular equipment/trinket mod (repo branch may need 1.20.1 tag) |
| 8 | `modern_industrialization` | https://github.com/AztechMC/Modern-Industrialization.git | `main` | 310 | 20M+ CF downloads; storage, technology, utility; ~310 PNG |
| 9 | `storage_delight` | https://github.com/axperty/storagedelight.git | `main` | 200 | 17M CF; Farmer's Delight storage addon |
| 10 | `iron_furnaces` | https://github.com/Qelifern/IronFurnaces.git | `main` | 180 | 96M CF; tiered furnace blocks and GUIs |
| 11 | `rftools_utility` | https://github.com/McJtyMods/RFToolsUtility.git | `main` | 180 | McJty suite; machines + screens in ATM10 |
| 12 | `integrated_terminals` | https://github.com/CyclopsMC/IntegratedTerminals.git | `main` | 110 | 57M CF; CyclopsMC AE-style terminals addon |
| 13 | `rftools_base` | https://github.com/McJtyMods/RFToolsBase.git | `main` | 120 | 50M+ CF downloads; technology, transportation; ~120 PNG |
| 14 | `reliquified_artifacts` | https://github.com/Octo-Studios/rar-compat.git | `main` | 110 | 24M CF; Artifacts compat layer, ATM10 QoL gear |
| 15 | `extrastorage` | https://github.com/Edivad99/ExtraStorage.git | `main` | 80 | 49M CF; Refined Storage expansion disks/parts |

## Runners-up (#16–25)

| mod_id | repo_url | branch | est_png_count | note |
|--------|----------|--------|--------------:|------|
| `ars_energistique` | https://github.com/62832/ArsEnergistique.git | `main` | 85 | 32M CF; Ars Nouveau + AE2 bridge (Ars already upscaled) |
| `rftools_storage` | https://github.com/McJtyMods/RFToolsStorage.git | `main` | 95 | 20M+ CF downloads; storage, technology; ~95 PNG |
| `wireless_chargers` | https://github.com/SuperMartijn642/WirelessChargers.git | `main` | 35 | 28M CF; SuperMartijn642 wireless charging blocks |
| `functional_storage` | https://github.com/Buuz135/FunctionalStorage.git | `main` | 140 | 54M CF; drawer-style storage blocks |
| `creeper_overhaul` | https://github.com/bonsaistudi0s/Creeper-Overhaul.git | `main` | 95 | 87M CF; biome-themed creeper mob variants |
| `modularrouters` | https://github.com/desht/ModularRouters.git | `1.20.1` | 85 | 69M CF; logistics router blocks and upgrades |
| `ars_ocultas` | https://github.com/dphaldes/Ars-Ocultas.git | `main` | 75 | 20M+ CF downloads; adventure, game-mechanics, magic; ~75 PNG |
| `dimstorage` | https://github.com/Edivad99/DimStorage.git | `main` | 45 | 31M CF; dimensional chest storage |
| `connectedglass` | https://github.com/SuperMartijn642/ConnectedGlass.git | `main` | 90 | 67M CF; many glass variants, quick win (~90 PNG) |
| `cpm_fabric` | https://github.com/AlphaMode/CompactMachines.git | `main` | ? | 50M+ CF downloads; storage, technology, utility; texture count TBD |

## Notes

- **Draconic Evolution** (`draconic_evolution`) is in ATM10 but already upscaled as `draconicevolution/`.
- **Twilight Forest** is upscaled as `twilightforest/`; ATM10 slug is `the_twilight_forest`.
- **Macaw's** mods are in `MOD_REPOS` but sourced from Modrinth JARs (`MODRINTH_JAR_MODS`) — already upscaled.
- Branches target **1.20.1 / 1.20.x Forge** to match the existing clone pipeline; ATM10 official pack is **1.21 NeoForge**.
- Mods without `source_url` / `MOD_REPOS` entry are omitted (112 in ATM10 list).

## Add to `config/registry.py`

These top candidates are **not** yet in `MOD_REPOS`:

- ~~`oh_the_biomes_weve_gone`~~ **DONE** (`biomeswevegone`, 1114 PNG)
- `railcraft_reborn` → `https://github.com/railcraft-reborn/railcraft.git` (`main`)
- `eternal_starlight` → `https://github.com/LeoMinecraftModding/eternal-starlight.git` (`main`)
- `the_undergarden` → `https://github.com/quek04/The-Undergarden.git` (`main`)
- `productivetrees` → `https://github.com/JDKDigital/productivetrees.git` (`main`)
- `extreme_reactors` → `https://github.com/ZeroNoRyouki/ExtremeReactors2.git` (`main`)
- `relics_mod` → `https://github.com/SSKirillSS/relics.git` (`main`)
- `modern_industrialization` → `https://github.com/AztechMC/Modern-Industrialization.git` (`main`)
- `storage_delight` → `https://github.com/axperty/storagedelight.git` (`main`)
- `iron_furnaces` → `https://github.com/Qelifern/IronFurnaces.git` (`main`)
- `rftools_utility` → `https://github.com/McJtyMods/RFToolsUtility.git` (`main`)
- `integrated_terminals` → `https://github.com/CyclopsMC/IntegratedTerminals.git` (`main`)
- `rftools_base` → `https://github.com/McJtyMods/RFToolsBase.git` (`main`)
- `reliquified_artifacts` → `https://github.com/Octo-Studios/rar-compat.git` (`main`)
- `extrastorage` → `https://github.com/Edivad99/ExtraStorage.git` (`main`)
