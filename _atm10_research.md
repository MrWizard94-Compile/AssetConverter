# ATM10 Mod Research

> **Version note:** Official ATM10 (`AllTheMods/ATM-10`, CurseForge) runs **Minecraft 1.21.x on NeoForge** — there is no ATM10 release for **1.20.1 Forge**. Branches below target **1.20.1 / 1.20.x** where your upscaling pipeline and cloned sources already use those versions.

Mod list source: [modpackindex.com ATM10 API](https://www.modpackindex.com/api/v1/modpack/85233/mods) (477 mods, synced June 2026). GitHub repo `AllTheMods/ATM-10` contains configs/kubejs only — no `manifest.json` or `mods/` folder.

## Summary

| Metric | Count |
|--------|------:|
| **Total ATM10 mods** | **477** |
| Unique normalized mod IDs | 477 |
| **Already covered** (matched to `output/assets`) | **29** |
| Library / utility / perf (excluded) | 136 |
| **NEW texture candidates** (public repo) | **200** |
| No public source URL | 112 |

## Already Covered

**52 namespaces** in `output/assets/`. **29** appear in the ATM10 mod list:

```
ae2, aether, apotheosis, ars_nouveau, bellsandwhistles, chipped, create, create_aquatic_ambitions, create_dragons_plus, create_enchantment_industry, create_hypertube, createaddition, deeperdarker, farmersdelight, iceandfire, immersiveengineering, irons_spellbooks, mekanism, mekanism_covers, mekanismgenerators, mekanismmoremachine, mekanismtools, minecolonies, mysticalagriculture, rechiseled, refinedstorage, sophisticatedbackpacks, supplementaries, twilightforest
```

**Upscaled mods NOT in ATM10** (26): classic 1.20.1 Forge content dropped or replaced in the 1.21 pack — e.g. Botania, Quark, Tinkers, Biomes O' Plenty, Alex's Caves, many Create addons.

```
alexscaves, another_furniture, biomesoplenty, botania, brewinandchewin, copycats, create_central_kitchen, create_connected, create_jetpack, create_new_age, create_sa, createbigcannons, createdeco, createendertransmission, createoreexcavation, interiors, mowziesmobs, quark, railways, sliceanddice, storagedrawers, tconstruct, thermal, trackwork, valkyrienskies, vs_clockwork
```

## Top 30 NEW Mods to Add

Prioritized by texture count + content categories. Excludes libraries/QoL/performance mods.

| mod_id | repo_url | branch | ~png_count |
|--------|----------|--------|----------:|
| `handcrafted` | https://github.com/terrarium-earth/Handcrafted.git | `1.20.1` | 1009 |
| `actuallyadditions` | https://github.com/Ellpeck/ActuallyAdditions.git | `1.20.x` | 850 |
| `occultism` | https://github.com/klikli-dev/occultism.git | `1.20.1` | 620 |
| `draconic_evolution` | https://github.com/Draconic-Inc/Draconic-Evolution.git | `1.20.1` | 520 |
| `pneumaticcraft` | https://github.com/TeamPneumatic/pnc-repressurized.git | `1.20.1` | 525 |
| `securitycraft` | https://github.com/Geforce132/SecurityCraft.git | `1.20.1` | 390 |
| `forbidden_arcanus` | https://github.com/MortuusArt/Forbidden-Arcanus.git | `1.20.1` | 320 |
| `evilcraft` | https://github.com/CyclopsMC/EvilCraft.git | `1.20.1` | 410 |
| `industrialforegoing` | https://github.com/InnovativeOnlineIndustries/Industrial-Foregoing.git | `release-1.20` | 370 |
| `integrateddynamics` | https://github.com/CyclopsMC/IntegratedDynamics.git | `1.20.1` | 430 |
| `enderio` | https://github.com/Team-EnderIO/EnderIO.git | `1.20.1` | 236 |
| `mcwroofs` | https://github.com/sketchmacaw/macawsroofs.git | `1.20.1` | 350 |
| `mcwdoors` | https://github.com/sketchmacaw/macawsdoors.git | `1.20.1` | 320 |
| `reliquary` | https://github.com/P3pp3rF1y/Reliquary.git | `1.20.1` | 210 |
| `productivebees` | https://github.com/CreativeMD/Production-Bees.git | `1.20.1` | 280 |
| `cookingforblockheads` | https://github.com/TwelveIterations/CookingForBlockheads.git | `1.20.1` | 240 |
| `sophisticatedstorage` | https://github.com/P3pp3rF1y/SophisticatedStorage.git | `1.20.x` | 315 |
| `mcwfences` | https://github.com/sketchmacaw/macawsfencesandgates.git | `1.20.1` | 260 |
| `aquaculture` | https://github.com/TeamMetallurgy/Aquaculture.git | `1.20.1` | 160 |
| `mcwwindows` | https://github.com/sketchmacaw/macawswindows.git | `1.20.1` | 200 |
| `mysticalagradditions` | https://github.com/BlakeBr0/MysticalAgradditions.git | `1.20.1` | 95 |
| `waystones` | https://github.com/TwelveIterations/Waystones.git | `1.20.1` | 55 |
| `mcwbridges` | https://github.com/sketchmacaw/macawsbridges.git | `1.20.1` | 180 |
| `trashcans` | https://github.com/SuperMartijn642/TrashCans.git | `main` | 40 |
| `ironjetpacks` | https://github.com/BlakeBr0/IronJetpacks.git | `1.20.1` | 70 |
| `artifacts` | https://github.com/ochotonida/artifacts.git | `1.20.1` | 120 |
| `mcwlights` | https://github.com/sketchmacaw/macawslightsandlamps.git | `1.20.1` | 150 |
| `xnet` | https://github.com/McJtyMods/XNet.git | `1.20.1` | 90 |
| `yungs_better_mineshafts` | https://github.com/YUNG-GANG/YUNGs-Better-Mineshafts.git | `1.20.1` | 30 |
| `yungs_better_dungeons` | https://github.com/YUNG-GANG/YUNGs-Better-Dungeons.git | `1.20.1` | 25 |

## Notable NEW Candidates (#31–50)

| mod_id | repo_url | branch | ~png_count |
|--------|----------|--------|----------:|
| `wireless_chargers` | https://github.com/SuperMartijn642/WirelessChargers | `main` | ? |
| `yungs_better_strongholds` | https://github.com/YUNG-GANG/YUNGs-Better-Strongholds.git | `1.20.1` | 20 |
| `simple_magnets` | https://github.com/SuperMartijn642/SimpleMagnets | `main` | ? |
| `relics_mod` | https://github.com/SSKirillSS/relics/tree/1.18.2 | `main` | ? |
| `reliquified_artifacts` | https://github.com/Octo-Studios/rar-compat | `main` | ? |
| `yungs_better_ocean_monuments` | https://github.com/YUNG-GANG/YUNGs-Better-Ocean-Monuments.git | `1.20.1` | 15 |
| `yungs_better_nether_fortresses` | https://github.com/YUNG-GANG/YUNGs-Better-Fortresses.git | `1.20.1` | 15 |
| `comforts` | https://github.com/illusivesoulworks/comforts.git | `1.20.1` | 45 |
| `fluxnetworks` | https://github.com/SonarSonic/Flux-Networks.git | `1.20.1` | 55 |
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