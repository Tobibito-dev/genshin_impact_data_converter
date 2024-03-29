paths = {
    'codex': 'ExcelBinOutput/ReliquaryCodexExcelConfigData.json',
    'set': 'ExcelBinOutput/ReliquarySetExcelConfigData.json',
    'artifact': 'ExcelBinOutput/ReliquaryExcelConfigData.json',
    'equipAffix': 'ExcelBinOutput/EquipAffixExcelConfigData.json',
    'displayItem': 'ExcelBinOutput/DisplayItemExcelConfigData.json',
    'ability': 'BinOutput/Ability/Temp/EquipAbilities/ConfigAbility_Relic.json',
}

template = {
    "templateType": "artifact",
    "id": "$suitId",
    "sortId": "$SortOrder",
    "name": "$suitId/displayItem/.param/#0/nameTextMapHash/text_map",
    "icon": "$suitId/displayItem/.param/#0/icon",

    "setRequirement": "$suitId/set/.setId/setNeedNum",
    "setAbilities": "$suitId/set/.setId/AKAIKNIJEKJ",
    "containsIds": "$suitId/set/.setId/containsList",
    "textList": "$suitId/set/.setId/textList",

    "setEffects": {
        "$suitId/set/.setId/setNeedNum/*": {
            "readable": {
                "openConfig": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/*/openConfig",
                "description": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/*/descTextMapHash/text_map",
            },
            "data": {
                "props": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/*/addProps",
                "parameters": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/*/paramList",
                "ability": "$suitId/set/.setId/EquipAffixId/equipAffix/.id/*/openConfig/ability/.Default.abilityName/Default",
            }
        }
    },



    "setPieces": {
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
    },
}
