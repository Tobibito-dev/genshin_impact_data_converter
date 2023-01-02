# common paths
common_path = 'ExcelBinOutput/EquipAffixExcelConfigData.json'

template = {
    'type': 'common',
    'paths': {'main': common_path},
    'data': {'name': {'path': 'main', 'key': 'nameTextMapHash', 'conversionMethod': 'textMap'},
             'id': {'path': 'main', 'key': 'id', 'conversionMethod': 'direct'}}
}
