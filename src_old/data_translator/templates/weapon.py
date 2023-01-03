# weapon paths
weapon_path = 'ExcelBinOutput/WeaponExcelConfigData.json'
weapon_curve_path = 'ExcelBinOutput/WeaponCurveExcelConfigData.json'
weapon_promote_path = 'ExcelBinOutput/WeaponPromoteExcelConfigData.json'
weapon_exp_data = 'ExcelBinOutput/WeaponPLevelExcelConfigData.json'
weapon_codex_path = 'ExcelBinOutput/WeaponCodexExcelConfigData.json'

template = {
    'type': 'weapon',
    'paths': {'main': weapon_path,
              'codex': weapon_codex_path,
              'sub0': weapon_curve_path,
              'sub1': weapon_promote_path,
              },
    'data': {'name': {'path': 'main', 'key': 'nameTextMapHash', 'conversionMethod': 'textMap'},
             'id': {'path': 'main', 'key': 'id', 'conversionMethod': 'direct'},
             'type': {'path': 'main', 'key': 'weaponType', 'conversionMethod': 'direct'},
             'rankLevel': {'path': 'main', 'key': 'rankLevel', 'conversionMethod': 'direct'},
             'baseStats': {'path': 'main', 'key': 'weaponProp', 'conversionMethod': 'baseStat'},
             'curve': {'path': 'sub0', 'key': 'weaponProp', 'conversionMethod': 'curve'},
             'promote': {'path': 'sub1', 'key': 'weaponPromoteId', 'conversionMethod': 'promote'},
             # Todo: weaponPromote and Weapon Affix
             'desc': {'path': 'main', 'key': 'descTextMapHash', 'conversionMethod': 'textMap'},
             'flavor': {'path': 'main', 'key': 'id', 'conversionMethod': 'readable'}
             }
}