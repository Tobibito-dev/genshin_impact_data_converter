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
    "qualityType": "$weaponId/weapon/.id/qualityType",
    "weaponType": "$weaponId/weapon/.id/weaponType",
    "baseStats":  "{weaponId/weapon/.id/weaponProp/*propType:weaponId/weapon/.id/weaponProp/*initValue}",
    "baseStats2": "[weaponId/weapon/.id/weaponProp/*propType]"
}
