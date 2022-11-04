# weapon paths
weapon_path = 'ExcelBinOutput/WeaponExcelConfigData.json'
weapon_curve_path = 'ExcelBinOutput/WeaponCurveExcelConfigData.json'
weapon_promote_path = 'ExcelBinOutput/WeaponPromoteExcelConfigData.json'
weapon_exp_data = 'ExcelBinOutput/WeaponPLevelExcelConfigData.json'

template = {
    'type': 'weapon',
    'paths': {'main': weapon_path,
              'sub0': weapon_curve_path,
              'sub1': weapon_promote_path,
              },
    'data': {'name': {'path': 'main', 'key': 'nameTextMapHash', 'conversionMethod': 'textMap'},
             'id': {'path': 'main', 'key': 'id', 'conversionMethod': 'direct'},
             'weaponType': {'path': 'main', 'key': 'weaponType', 'conversionMethod': 'direct'},
             'rankLevel': {'path': 'main', 'key': 'rankLevel', 'conversionMethod': 'direct'},
             'weaponDesc': {'path': 'main', 'key': 'descTextMapHash', 'conversionMethod': 'textMap'},
             # 'weaponStats': {},
             # 'weaponPromote': {},
             'weaponFlavor': {'path': 'main', 'key': 'id', 'conversionMethod': 'readable'}
             # TODO: weapon template
             }
}