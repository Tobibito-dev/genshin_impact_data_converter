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
    "id": "$avatarId",
    "sortId": "$sortId",
    "name": "$avatarId/character/.id/nameTextMapHash/text_map",
    "icon": "$avatarId/character/.id/iconName",
    "sideIcon": "$avatarId/character/.id/sideIconName",
    "qualityType": "$avatarId/character/.id/qualityType",
    "weaponType": "$avatarId/character/.id/weaponType",
    "baseStats": {
        "$avatarId/character/.id/propGrowCurves/#0/type": "$avatarId/character/.id/hpBase",
        "$avatarId/character/.id/propGrowCurves/#1/type": "$avatarId/character/.id/attackBase",
        "$avatarId/character/.id/propGrowCurves/#2/type": "$avatarId/character/.id/defenseBase"
    },
    "curve": {"$curve/*/level": {
        "$avatarId/character/.id/propGrowCurves/#0/type": {
            "value": "$avatarId/character/.id/propGrowCurves/#0/growCurve/curve/*/curveInfos/.type/value",
            "arith": "$avatarId/character/.id/propGrowCurves/#0/growCurve/curve/*/curveInfos/.type/arith"
        },
        "$avatarId/character/.id/propGrowCurves/#1/type": {
            "value": "$avatarId/character/.id/propGrowCurves/#1/growCurve/curve/*/curveInfos/.type/value",
            "arith": "$avatarId/character/.id/propGrowCurves/#1/growCurve/curve/*/curveInfos/.type/arith"
        },
        "$avatarId/character/.id/propGrowCurves/#2/type": {
            "value": "$avatarId/character/.id/propGrowCurves/#2/growCurve/curve/*/curveInfos/.type/value",
            "arith": "$avatarId/character/.id/propGrowCurves/#2/growCurve/curve/*/curveInfos/.type/arith"
        },
    }}
    # "promote": {},
    # skill
    # burst
    # passives
    # cons
}
