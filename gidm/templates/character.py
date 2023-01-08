paths = {
    "codex": 'ExcelBinOutput/AvatarCodexExcelConfigData.json',
    "character": 'ExcelBinOutput/AvatarExcelConfigData.json',
    "curve": 'ExcelBinOutput/AvatarCurveExcelConfigData.json',
    "promote": 'ExcelBinOutput/AvatarPromoteExcelConfigData.json',
    "constellation": 'ExcelBinOutput/AvatarTalentExcelConfigData.json',
    "passive": 'ExcelBinOutput/ProudSkillExcelConfigData.json',
    "skill_depot": 'ExcelBinOutput/AvatarSkillDepotExcelConfigData.json',
    "talent": 'ExcelBinOutput/AvatarSkillExcelConfigData.json'
}

template = {
    "templateType": "character",
    "avatarId": "$avatarId",
    "name": "$avatarId/character/.id/nameTextMapHash/text_map",
    "icon": "$avatarId/character/.id/iconName",
    "sideIcon": "$avatarId/character/.id/sideIconName",
    "qualityType": "$avatarId/character/.id/qualityType",
    "weaponType": "$avatarId/character/.id/weaponType",
    "baseStats": {
        "FIGHT_PROP_BASE_HP": "$avatarId/character/.id/hpBase",
        "FIGHT_PROP_BASE_ATTACK": "$avatarId/character/.id/attackBase",
        "FIGHT_PROP_BASE_DEFENSE": "$avatarId/character/.id/defenseBase"
    },
    #"curve": {"":[
    #    {
    #        "type": "#FIGHT_PROP_BASE_HP",
    #        "value": "avatarId/character/.id/propGrowCurves/.type=FIGHT_PROP_BASE_HP/growCurve/curve/.level/curveInfos/.type/value",
    #        "arith": ""
    #    },
    #    {
    #        "type": "#FIGHT_PROP_BASE_ATTACK",
    #    },
    #    {
    #        "type": "#FIGHT_PROP_BASE_DEFENSE",
    #    }
    #]},
    # "promote": {},
    # skill
    # burst
    # passives
    # cons
}
