# character paths
character_path = 'ExcelBinOutput/AvatarExcelConfigData.json'
character_curve_path = 'ExcelBinOutput/AvatarCurveExcelConfigData.json'
character_promote_path = 'ExcelBinOutput/AvatarPromoteExcelConfigData.json'
character_constellations_path = 'ExcelBinOutput/AvatarTalentExcelConfigData.json'
character_passives_path = 'ExcelBinOutput/ProudSkillExcelConfigData.json'
character_skill_depot_path = 'ExcelBinOutput/AvatarSkillDepotExcelConfigData.json'
character_talents_path = 'ExcelBinOutput/AvatarSkillExcelConfigData.json'
character_codex_path = 'ExcelBinOutput/AvatarCodexExcelConfigData.json'

template = {
    'type': 'character',
    'paths': {'main': character_path,
              'codex': character_codex_path,
              'curve': character_curve_path,
              'promote': character_promote_path,
              'depot': character_skill_depot_path,
              'constellations': character_constellations_path,
              'passives': character_passives_path,
              'talents': character_talents_path,},
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
             'curve': {'path': 'curve', 'key': 'propGrowCurves', 'conversionMethod': 'curve'},
             'promote': {'path': 'promote', 'key': 'avatarPromoteId', 'conversionMethod': 'promote'},
             'talents': {'path': 'depot', 'key': 'skills', 'conversionMethod': 'talent'}
             # TODO: character talents
             }
}
