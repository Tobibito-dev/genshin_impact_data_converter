# artifact paths
artifact_path = 'ExcelBinOutput/ReliquaryExcelConfigData.json'
artifact_set_path = 'ExcelBinOutput/ReliquarySetExcelConfigData.json'
artifact_mainstat_path = 'ExcelBinOutput/ReliquaryLevelExcelConfigData.json'
artifact_substat_path = 'ExcelBinOutput/ReliquaryAffixExcelConfigData.json'

template = {
    'type': 'character',
    'paths': {'main': artifact_path},
    'data': {'name': {'path': 'main', 'key': 'nameTextMapHash', 'conversionMethod': 'textMap'},
             }
}
