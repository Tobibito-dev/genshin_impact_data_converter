# get character specific ids
from characters import char
# get skill ids
from dmg_sheet import sheet

ids = {
    # add char and sheet
    "char": char,
    "sheet": sheet,

    # these will be automatically filled
    "character_names": {},
    "weapon":  {},
    "weapon_names": {},
    "artifact": {},
    "artifact_names": {},
    "material": {},




    "weapon_key": {
        "sword": 1338971918,
        "polearm": 1654223994,
        "bow": 4066070434,
        "claymore": 2037297130,
        "catalyst": 43479985
    },

    "elemental_resonance": {
        "protective_canopy": {
            "name": 2109006394,
            "desc": 3981421851
        },
        "fervent_flames": {
            "name": 2012776706,
            "desc": 3981421851
        },
        "soothing_water": {
            "name": 2733620714,
            "desc": 740980787
        },
        "shattering_ice": {
            "name": 1853529306,
            "desc": 2601161539
        },
        "high_voltage": {
            "name": 2331327954,
            "desc": 1982396323
        },
        "impetuous_winds": {
            "name": 166087994,
            "desc": 170982675
        },
        "enduring_rock": {
            "name": 3018382842,
            "desc": 1707021043
        },
        "sprawling_greenery": {
            "name": 1292621586,
            "desc": 2900013027
        },
    },
}