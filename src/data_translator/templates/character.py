# character paths
character_path = 'ExcelBinOutput/AvatarExcelConfigData.json'
character_curve_path = 'ExcelBinOutput/AvatarCurveExcelConfigData.json'
character_promote_path = 'ExcelBinOutput/AvatarPromoteExcelConfigData.json'
character_constellations_path = 'ExcelBinOutput/AvatarTalentExcelConfigData.json'
character_passives_path = 'ExcelBinOutput/ProudSkillExcelConfigData.json'
character_skill_depot_path = 'ExcelBinOutput/AvatarSkillDepotExcelConfigData.json'
character_talents_path = 'ExcelBinOutput/AvatarSkillExcelConfigData.json'

template = {
    'type': 'character',
    'paths': {'main': character_path,
              'sub0': character_curve_path,
              'sub1': character_promote_path,
              'depot': character_skill_depot_path,
              'sub2': character_constellations_path,
              'sub3': character_passives_path,
              'sub4': character_talents_path,},
    'data': {'name': {'path': 'main', 'key': 'nameTextMapHash', 'conversionMethod': 'textMap'},
             'id': {'path': 'main', 'key': 'id', 'conversionMethod': 'direct'},
             'useType': {'path': 'main', 'key': 'useType', 'conversionMethod': 'direct'},
             'bodyType': {'path': 'main', 'key': 'bodyType', 'conversionMethod': 'direct'},
             'iconName': {'path': 'main', 'key': 'iconName', 'conversionMethod': 'direct'},
             'sideIconName': {'path': 'main', 'key': 'sideIconName', 'conversionMethod': 'direct'},
             'qualityType': {'path': 'main', 'key': 'qualityType', 'conversionMethod': 'direct'},
             'weaponType': {'path': 'main', 'key': 'weaponType', 'conversionMethod': 'direct'},
             'baseStats': {'path': 'main', 'key': 'propGrowCurves', 'conversionMethod': 'baseStat',
                           'key_list': ['hpBase', 'attackBase', 'defenseBase']},
             'curve': {'path': 'sub0', 'key': 'propGrowCurves', 'conversionMethod': 'curve'},
             'promote': {'path': 'sub1', 'key': 'avatarPromoteId', 'conversionMethod': 'promote'},
             'talents': {'path': 'depot', 'key': 'skillDepotId', 'conversionMethod': 'talent'}
             # TODO: character talents
             }
}
