# material paths
material_path = 'ExcelBinOutput/MaterialExcelConfigData.json'
material_codex_path = 'ExcelBinOutput/MaterialCodexExcelConfigData.json'

template = {
    'type': 'material',
    'paths': {'main': material_path, 'codex': material_codex_path},
    'data': {'name': {'path': 'main', 'key': 'nameTextMapHash', 'conversionMethod': 'textMap'},
             'id': {'path': 'main', 'key': 'id', 'conversionMethod': 'direct'},
             'materialDesc': {'path': 'main', 'key': 'descTextMapHash', 'conversionMethod': 'textMap'},
             'materialType': {'path': 'main', 'key': 'materialType', 'conversionMethod': 'direct'}}
}
