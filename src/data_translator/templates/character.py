# character paths
character_path = 'ExcelBinOutput/AvatarExcelConfigData.json'
character_curve_path = 'ExcelBinOutput/AvatarCurveExcelConfigData.json'
character_promote_path = 'ExcelBinOutput/AvatarPromoteExcelConfigData.json'
character_friendship_path = 'ExcelBinOutput/FetterCharacterCardExcelConfigData'
character_reward_path = 'ExcelBinOutput/RewardExcelConfigData.json'
character_info_path = 'ExcelBinOutput//FetterInfoExcelConfigData'
character_constellations_path = 'ExcelBinOutput/AvatarTalentExcelConfigData.json'
character_passives_path = 'ExcelBinOutput/ProudSkillExcelConfigData.json'
character_skill_depot_path = 'ExcelBinOutput/AvatarSkillDepotExcelConfigData.json'
character_talents_path = 'ExcelBinOutput/AvatarSkillExcelConfigData.json'
character_materials_path = 'ExcelBinOutput/MaterialExcelConfigData.json'

template = {
    'type': 'character',
    'paths': {'main': character_path,
              'sub0': character_curve_path},
    'data': {'name': {'path': 'main', 'key': 'nameTextMapHash', 'conversionMethod': 'textMap'},
             'id': {'path': 'main', 'key': 'id', 'conversionMethod': 'direct'},
             'baseStats': {'path': 'main', 'key': 'propGrowCurves', 'conversionMethod': 'stat',
                           'key_list': ['hpBase', 'attackBase', 'defenseBase']},
             'curve': {'path': 'sub0', 'key': 'propGrowCurves', 'conversionMethod': 'curve'},
             }
}
