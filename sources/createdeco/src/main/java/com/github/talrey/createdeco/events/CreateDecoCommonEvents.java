package com.github.talrey.createdeco.events;

import com.github.talrey.createdeco.blocks.ShippingContainerBlock;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.neoforge.capabilities.RegisterCapabilitiesEvent;

@EventBusSubscriber
public class CreateDecoCommonEvents {

	@SubscribeEvent
	private static void registerCapabilities(RegisterCapabilitiesEvent event) {
		ShippingContainerBlock.Entity.registerCapabilities(event);
	}
}
