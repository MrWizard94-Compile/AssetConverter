# ATM10 Mod Research

> **Version note:** Official ATM10 (`AllTheMods/ATM-10`, CurseForge) runs **Minecraft 1.21.x on NeoForge** — there is no ATM10 release for **1.20.1 Forge**. Branches below target **1.20.1 / 1.20.x** where your upscaling pipeline and cloned sources already use those versions.

Mod list source: [modpackindex.com ATM10 API](https://www.modpackindex.com/api/v1/modpack/85233/mods) (477 mods, synced June 2026). GitHub repo `AllTheMods/ATM-10` contains configs/kubejs only — no `manifest.json` or `mods/` folder.

## Summary

| Metric | Count |
|--------|------:|
| **Total ATM10 mods** | **477** |
| Unique normalized mod IDs | 477 |
| **Already covered** (matched to `output/assets`) | **58** |
| Library / utility / perf (excluded) | 136 |
| **NEW texture candidates** (public repo) | **171** |
| No public source URL | 112 |

## Already Covered

**84 namespaces** in `output/assets/`. **58** appear in the ATM10 mod list:

```
actuallyadditions, ae2, aether, apotheosis, aquaculture, ars_nouveau, artifacts, bellsandwhistles, chipped, comforts, cookingforblockheads, create, create_aquatic_ambitions, create_dragons_plus, create_enchantment_industry, create_hypertube, createaddition, deeperdarker, enderio, evilcraft, farmersdelight, fluxnetworks, forbidden_arcanus, handcrafted, iceandfire, immersiveengineering, industrialforegoing, integrateddynamics, ironjetpacks, irons_spellbooks, mcwbridges, mcwdoors, mcwfences, mcwlights, mcwroofs, mcwwindows, mekanism, mekanism_covers, mekanismgenerators, mekanismmoremachine, mekanismtools, minecolonies, mysticalagradditions, mysticalagriculture, occultism, pneumaticcraft, productivebees, rechiseled, refinedstorage, reliquary, securitycraft, sophisticatedbackpacks, sophisticatedstorage, supplementaries, trashcans, twilightforest, waystones, xnet
```

**Upscaled mods NOT in ATM10** (28): classic 1.20.1 Forge content dropped or replaced in the 1.21 pack — e.g. Botania, Quark, Tinkers, Biomes O' Plenty, Alex's Caves, many Create addons.

```
alexscaves, another_furniture, biomesoplenty, biomeswevegone, botania, brewinandchewin, copycats, create_central_kitchen, create_connected, create_jetpack, create_new_age, create_sa, createbigcannons, createdeco, createendertransmission, createoreexcavation, draconicevolution, interiors, mowziesmobs, quark, railways, sliceanddice, storagedrawers, tconstruct, thermal, trackwork, valkyrienskies, vs_clockwork
```

## Top 30 NEW Mods to Add

Prioritized by texture count + content categories. Excludes libraries/QoL/performance mods.

| mod_id | repo_url | branch | ~png_count |
|--------|----------|--------|----------:|
| `oh_the_biomes_weve_gone` | https://github.com/Potion-Studios/Oh-The-Biomes-Weve-Gone.git | `main` | 1114 |
| `draconic_evolution` | https://github.com/Draconic-Inc/Draconic-Evolution.git | `1.20.1` | 520 |
| `yungs_better_mineshafts` | https://github.com/YUNG-GANG/YUNGs-Better-Mineshafts.git | `1.20.1` | 30 |
| `yungs_better_dungeons` | https://github.com/YUNG-GANG/YUNGs-Better-Dungeons.git | `1.20.1` | 25 |
| `wireless_chargers` | https://github.com/SuperMartijn642/WirelessChargers | `main` | ? |
| `yungs_better_strongholds` | https://github.com/YUNG-GANG/YUNGs-Better-Strongholds.git | `1.20.1` | 20 |
| `simple_magnets` | https://github.com/SuperMartijn642/SimpleMagnets | `main` | ? |
| `relics_mod` | https://github.com/SSKirillSS/relics.git | `main` | ? |
| `reliquified_artifacts` | https://github.com/Octo-Studios/rar-compat.git | `main` | ? |
| `yungs_better_ocean_monuments` | https://github.com/YUNG-GANG/YUNGs-Better-Ocean-Monuments.git | `1.20.1` | 15 |
| `yungs_better_nether_fortresses` | https://github.com/YUNG-GANG/YUNGs-Better-Fortresses.git | `1.20.1` | 15 |
| `mo_structures` | https://github.com/frqnny/mostructures | `main` | ? |
| `yungs_extras` | https://github.com/YUNG-GANG/YUNGs-Extras.git | `1.20.1` | ? |
| `yungs_better_desert_temples` | https://github.com/YUNG-GANG/YUNGs-Better-Desert-Temples.git | `1.20.1` | ? |
| `yungs_better_witch_huts` | https://github.com/YUNG-GANG/YUNGs-Better-Witch-Huts.git | `1.20.1` | ? |
| `structory` | https://github.com/Stardust-Labs-MC/Structory | `main` | ? |
| `moogs_voyager_structures` | https://github.com/Moog-s-Mods/MoogsVoyagerStructures | `main` | ? |
| `structory_towers` | https://github.com/Stardust-Labs-MC/Structory-Towers | `main` | ? |
| `mes_moogs_end_structures` | https://github.com/FinnSetchell/MoogsEndStructures | `main` | ? |
| `yungs_better_jungle_temples` | https://github.com/YUNG-GANG/YUNGs-Better-Jungle-Temples.git | `1.20.1` | ? |
| `yungs_better_end_island` | https://github.com/yungnickyoung/YUNGs-Better-End-Island.git | `1.20.1` | ? |
| `villages_and_pillages` | https://github.com/Faboslav/villages-and-pillages | `main` | ? |
| `modularrouters` | https://github.com/desht/ModularRouters.git | `1.20.1` | 85 |
| `integrated_terminals` | https://github.com/CyclopsMC/IntegratedTerminals.git | `main` | ? |
| `dimstorage` | https://github.com/Edivad99/DimStorage | `main` | ? |
| `entangled` | https://github.com/SuperMartijn642/Entangled | `main` | ? |
| `extrastorage` | https://github.com/Edivad99/ExtraStorage.git | `main` | ? |
| `universal_grid` | https://github.com/starforcraft/Universal-Grid | `main` | ? |
| `creeperhost_presents_steves_carts` | https://github.com/CreeperHost/StevesCarts2 | `main` | ? |
| `railcraft_reborn` | https://github.com/railcraft-reborn/railcraft.git | `main` | ? |

## Notable NEW Candidates (#31–50)

| mod_id | repo_url | branch | ~png_count |
|--------|----------|--------|----------:|
| `ars_energistique` | https://github.com/62832/ArsEnergistique | `main` | ? |
| `ars_ocultas` | https://github.com/dphaldes/Ars-Ocultas | `main` | ? |
| `apothic_spawners` | https://github.com/Shadows-of-Fire/Apothic-Spawners | `main` | ? |
| `connectedglass` | https://github.com/SuperMartijn642/ConnectedGlass.git | `main` | 90 |
| `storage_delight` | https://github.com/axperty/storagedelight.git | `main` | ? |
| `the_undergarden` | https://github.com/quek04/The-Undergarden.git | `main` | ? |
| `variants_and_ventures` | https://github.com/Faboslav/variants-and-ventures | `main` | ? |
| `eternal_starlight` | https://github.com/LeoMinecraftModding/eternal-starlight.git | `main` | ? |
| `pipez` | https://github.com/henkelmax/pipez.git | `1.20.1` | 45 |
| `extra_disks` | https://github.com/ChaoticTrials/ExtraDisks | `main` | ? |
| `cpm_fabric` | https://github.com/AlphaMode/CompactMachines | `main` | ? |
| `rftools_storage` | https://github.com/McJtyMods/RFToolsStorage | `main` | ? |
| `iron_furnaces` | https://github.com/Qelifern/IronFurnaces.git | `main` | ? |
| `ranged_pumps` | https://github.com/refinedmods/rangedpumps | `main` | ? |
| `rftools_utility` | https://github.com/McJtyMods/RFToolsUtility.git | `main` | ? |
| `extreme_reactors` | https://github.com/ZeroNoRyouki/ExtremeReactors2.git | `main` | ? |
| `rftools_base` | https://github.com/McJtyMods/RFToolsBase.git | `main` | ? |
| `item_collectors` | https://github.com/SuperMartijn642/ItemCollectors | `main` | ? |
| `modern_industrialization` | https://github.com/AztechMC/Modern-Industrialization.git | `main` | ? |
| `interdimensional_wireless_transmitter` | https://github.com/starforcraft/Interdimensional-Wireless-Transmitter | `main` | ? |

## No Public GitHub/GitLab Source

- `additional_lights` — Additional Lights
- `ae2_crafting_tree` — AE2: Crafting Tree
- `ae2_jei_integration` — AE2 JEI Integration
- `ae2_network_analyser` — AE2 Network Analyser
- `all_the_arcanist_gear` — All The Arcanist Gear
- `all_the_tweaks` — All The Tweaks
- `all_the_wizard_gear` — All the Wizard Gear
- `allthecompressed` — AllTheCompressed
- `alltheleaks` — AllTheLeaks (Memory Leak Fix)
- `allthemodium` — Allthemodium
- `amendments` — Amendments
- `apothic_enchanting` — Apothic Enchanting
- `applied_flux` — Applied Flux
- `ars_elemancy` — Ars Elemancy
- `ars_elemental` — Ars Elemental
- `ars_technica` — Ars Technica
- `ato` — ATO - All the Ores
- `auroras` — Auroras
- `blockui` — BlockUI
- `byzantine_styles_pack_for_minecolonies` — Byzantine Styles Pack for Minecolonies
- `camol` — Camol
- `cat_jammies` — Cat Jammies
- `cc_tweaked_remastered` — CC: Tweaked (Unofficial)
- `charging_gadgets` — Charging Gadgets
- `chroma_carvings` — Chroma Carvings
- `clean_swing_through_grass` — Clean Swing Through Grass
- `cobblegen_galore` — Cobblegen Galore
- `corail_tombstone` — Corail Tombstone
- `cosmetic_armor_reworked` — Cosmetic Armor Reworked
- `crash_utilities` — Crash Utilities
- `deimos_fabric_forge_neoforge` — Deimos Lib
- `domum_ornamentum` — Domum Ornamentum
- `dyenamics` — Dyenamics
- `dyson_cube_project` — Dyson Cube Project
- `ex_pattern_provider` — ExtendedAE