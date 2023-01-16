paths = {
    'codex': 'ExcelBinOutput/ReliquaryCodexExcelConfigData.json',
    'set': 'ExcelBinOutput/ReliquarySetExcelConfigData.json',
    'artifact': 'ExcelBinOutput/ReliquaryExcelConfigData.json',
    'equipAffix': 'ExcelBinOutput/EquipAffixExcelConfigData.json',
    'display_item': 'ExcelBinOutput/DisplayItemExcelConfigData.json'
}

template = {
    "templateType": "artifact",
    "id": "$suitId",
    "sortId": "$SortOrder",
    "equipAffixId": "$suitId/set/.setId/EquipAffixId",
    "name": "$suitId/display_item/.param/#0/nameTextMapHash/text_map",
    "icon": "$suitId/display_item/.param/#0/icon",

    "setRequirement": "$suitId/set/.setId/setNeedNum",
    "setAbilities": "$suitId/set/.setId/AKAIKNIJEKJ",
    "containsIds": "$suitId/set/.setId/containsList",
    "textList": "$suitId/set/.setId/textList",

    "setEffects": [
        {
            "openConfig": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/#0/openConfig",
            "description": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/#0/descTextMapHash/text_map",
            "props": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/#0/addProps",
            "parameters": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/#0/paramList",
        },
        {
            "openConfig": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/#1/openConfig",
            "description": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/#1/descTextMapHash/text_map",
            "props": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/#1/addProps",
            "parameters": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/#1/paramList",
            "level": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/#1/level"
        },
    ],
    "flower": {
        "name": "$flowerId/artifact/.id/nameTextMapHash/text_map",
        "id": "$flowerId",
        "icon": "$flowerId/artifact/.id/icon",
    },
    "feather": {
        "name": "$leatherId/artifact/.id/nameTextMapHash/text_map",
        "id": "$leatherId",
        "icon": "$leatherId/artifact/.id/icon",
    },
    "sands": {
        "name": "$sandId/artifact/.id/nameTextMapHash/text_map",
        "id": "$sandId",
        "icon": "$sandId/artifact/.id/icon",
    },
    "goblet": {
        "name": "$cupId/artifact/.id/nameTextMapHash/text_map",
        "id": "$cupId",
        "icon": "$cupId/artifact/.id/icon",
    },
    "circlet": {
        "name": "$capId/artifact/.id/nameTextMapHash/text_map",
        "id": "$capId",
        "icon": "$capId/artifact/.id/icon",
    },
}
