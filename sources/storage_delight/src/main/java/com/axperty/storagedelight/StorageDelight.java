package com.axperty.storagedelight;

import com.axperty.storagedelight.registry.*;
import com.mojang.logging.LogUtils;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import org.slf4j.Logger;

@Mod(StorageDelight.MOD_ID)
public class StorageDelight {
    public static final String MOD_ID = "storagedelight";
    public static final Logger LOGGER = LogUtils.getLogger();

    public StorageDelight(IEventBus modEventBus) {
        ItemRegistry.ITEMS.register(modEventBus);
        BlockRegistry.BLOCKS.register(modEventBus);
        EntityTypesRegistry.BLOCK_ENTITY_TYPES.register(modEventBus);
        CreativeTabRegistry.CREATIVE_MODE_TABS.register(modEventBus);
        LOGGER.info("Storage Delight loaded");
    }
}
