# common paths
common_path = 'ExcelBinOutput/EquipAffixExcelConfigData.json'

template = {
    'type': 'character',
    'paths': {'main': common_path},
    'data': {'name': {'path': 'main', 'key': 'nameTextMapHash', 'conversionMethod': 'textMap'},
             }
}
