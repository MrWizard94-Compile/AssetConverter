package com.chaosthedude.explorerscompass.sorting;

import com.chaosthedude.explorerscompass.ExplorersCompass;

import net.minecraft.client.resources.language.I18n;
import net.minecraft.resources.Identifier;

public class GroupSorting implements ISorting {
	
	@Override
	public int compare(Identifier key1, Identifier key2) {
		return ExplorersCompass.structureIdsToGroupIds.get(key1).compareTo(ExplorersCompass.structureIdsToGroupIds.get(key2));
	}

	@Override
	public Object getValue(Identifier key) {
		return ExplorersCompass.structureIdsToGroupIds.get(key);
	}

	@Override
	public ISorting next() {
		return new NameSorting();
	}

	@Override
	public String getLocalizedName() {
		return I18n.get("string.explorerscompass.group");
	}

}
