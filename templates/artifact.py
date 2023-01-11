paths = {
    'codex': 'ExcelBinOutput/ReliquaryCodexExcelConfigData.json',
    'set': 'ExcelBinOutput/ReliquarySetExcelConfigData.json',
    'artifact': 'ExcelBinOutput/ReliquaryExcelConfigData.json',
    'affix': 'ExcelBinOutput/EquipAffixExcelConfigData.json',
    'display_item': 'ExcelBinOutput/DisplayItemExcelConfigData.json'
}

template = {
    "templateType": "artifact",
    "id": "$suitId",
    "name": "$suitId/display_item/.param/#0/nameTextMapHash/text_map",
    "icon": "$suitId/display_item/.param/#0/icon",

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
