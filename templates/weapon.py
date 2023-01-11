paths = {
    "codex": 'ExcelBinOutput/WeaponCodexExcelConfigData.json',
    "weapon": 'ExcelBinOutput/WeaponExcelConfigData.json',
    "curve": 'ExcelBinOutput/WeaponCurveExcelConfigData.json',
    "promote": 'ExcelBinOutput/WeaponPromoteExcelConfigData.json'
}

template = {
    "templateType": "weapon",
    "id": "$weaponId",
    "name": "$weaponId/weapon/.id/nameTextMapHash/text_map",
    "icon": "$weaponId/weapon/.id/icon",
    "rankLevel": "$weaponId/weapon/.id/rankLevel",
    "weaponType": "$weaponId/weapon/.id/weaponType",
    "baseStat": {
        "$weaponId/weapon/.id/weaponProp/#0/propType": "$weaponId/weapon/.id/weaponProp/#0/initValue",
        "$weaponId/weapon/.id/weaponProp/#1/propType": "$weaponId/weapon/.id/weaponProp/#1/initValue",
    },
    "curve": {"$curve/*/level": {
        "$weaponId/weapon/.id/weaponProp/#0/propType": {
            "value": "$weaponId/weapon/.id/weaponProp/#0/type/curve/*/curveInfos/.type/value",
            "arith": "$weaponId/weapon/.id/weaponProp/#0/type/curve/*/curveInfos/.type/arith"
        },
        "$weaponId/weapon/.id/weaponProp/#1/propType": {
            "value": "$weaponId/weapon/.id/weaponProp/#1/type/curve/*/curveInfos/.type/value",
            "arith": "$weaponId/weapon/.id/weaponProp/#1/type/curve/*/curveInfos/.type/arith"
        }
    }}
}
