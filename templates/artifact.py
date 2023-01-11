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

    "flower": {
        "name": "$flowerId/artifact/.id/nameTextMapHash/text_map",
    },
    "feather": {
        "name": "$leatherId/artifact/.id/nameTextMapHash/text_map",
    },
    "sands": {
        "name": "$sandId/artifact/.id/nameTextMapHash/text_map",
    },
    "goblet": {
        "name": "$cupId/artifact/.id/nameTextMapHash/text_map",
    },
    "circlet": {
        "name": "$capId/artifact/.id/nameTextMapHash/text_map",
    },
}
