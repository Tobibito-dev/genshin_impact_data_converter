# artifact paths
artifact_path = 'ExcelBinOutput/ReliquaryExcelConfigData.json'
artifact_set_path = 'ExcelBinOutput/ReliquarySetExcelConfigData.json'
artifact_mainstat_path = 'ExcelBinOutput/ReliquaryLevelExcelConfigData.json'
artifact_substat_path = 'ExcelBinOutput/ReliquaryAffixExcelConfigData.json'

template = {
    'type': 'artifact',
    'paths': {'main': artifact_path},
    'data': {'name': {'path': 'main', 'key': 'nameTextMapHash', 'conversionMethod': 'textMap'},
             'id': {'path': 'main', 'key': 'id', 'conversionMethod': 'direct'},
             'setId': {'path': 'main', 'key': 'setId', 'conversionMethod': 'direct'},
             'itemType': {'path': 'main', 'key': 'itemType', 'conversionMethod': 'direct'},
             'equipType': {'path': 'main', 'key': 'equipType', 'conversionMethod': 'direct'},
             'rankLevel': {'path': 'main', 'key': 'rankLevel', 'conversionMethod': 'direct'},
             # TODO: artifact props
             'maxLevel': {'path': 'main', 'key': 'itemType', 'conversionMethod': 'direct'},
             # TODO: rest of artifacts
             }
}
