import json

from . import config_data_paths
from . import float_calculator
from . import text_map_util


def get_weapons(genshin_data_path: str, language):
    print('Translating weapons')
    weapon_data = prepare_weapon_data(genshin_data_path)
    weapon_promote_data = prepare_weapon_promote_data(genshin_data_path)
    weapon_curve_data = prepare_weapon_curve_data(genshin_data_path)

    # create weapons dict and set unknown to 0
    weapons = {}
    unknown = 0
    for weapon in weapon_data:
        # get weapon name in correct language
        name = text_map_util.get_value_from_language(language, str(weapon['nameTextMapHash']))
        # replace spaces in name with underscore and remove apostrophe
        key = str(name).lower().replace(' ', '_').replace("'", '')
        # check for key == none and replace
        if key == 'none':
            key = 'unknown' + str(unknown)
            unknown = unknown + 1

        # create new weapon object in dict with key
        weapons[key] = {'weaponName': name,
                        'weaponData': weapon,
                        'weaponStats': get_weapon_stats(weapon, weapon_curve_data)
                        }
        # print(get_weapon_stats(weapon, weapon_curve_data))

    # add amount of unknown weapon names
    weapons['unknownCount'] = unknown
    print(weapons['amos_bow']['weaponStats']['levels'][10])


# create weapon stats based on curve
def get_weapon_stats(weapon: dict, weapon_curve_data: list):
    # get base values
    main_stat_init = weapon['weaponProp'][0]
    sub_stat_init = weapon['weaponProp'][1]
    main_curve_type = main_stat_init['type']
    sub_stat_type = sub_stat_init['type']

    # initialize weapon stats, add stat types and add base stats add default value if not found
    weapon_stats = {
        'mainStatType': main_stat_init.get('propType', 'None'),
        'subStatType': sub_stat_init.get('propType', 'None'),
        'mainStatBase': main_stat_init.get('initValue', 0),
        'subStatBase': sub_stat_init.get('initValue', 0),
        'levels': {}
    }

    for level_data in weapon_curve_data:
        main_curve_value = level_data['curveInfos']['GROW_CURVE_ATTACK_203']['value']
        sub_curve_value = level_data['curveInfos']['GROW_CURVE_ATTACK_202']['value']

        # insert data for one level into weapon stats['levels']
        weapon_stats['levels'][level_data['level']] = {
            'mainStat': main_curve_value,
            'subStat': sub_curve_value
        }
    return weapon_stats


# currently no preparation needed
def prepare_weapon_data(genshin_data_path: str):
    temp_list = json.loads(open(genshin_data_path + config_data_paths.weapon_path).read())
    return temp_list


# assign promote id as key
def prepare_weapon_promote_data(genshin_data_path: str):
    temp_list = json.loads(open(genshin_data_path + config_data_paths.weapon_promote_path).read())
    temp_dict = {}
    for item in temp_list:
        # check for existing key and create if none found
        if item['weaponPromoteId'] not in temp_dict:
            temp_dict[item['weaponPromoteId']] = {}
        # if no promote level found assign promote level 0
        if 'promoteLevel' not in item:
            item['promoteLevel'] = 0
        # put in promote values with id and level as key
        temp_dict[item['weaponPromoteId']][item['promoteLevel']] = item
    return temp_dict


# add type as key for curve info
def prepare_weapon_curve_data(genshin_data_path: str):
    temp_list = json.loads(open(genshin_data_path + config_data_paths.weapon_curve_path).read())
    for level_data in temp_list:
        new_curve_info = {}
        for curve_info in level_data['curveInfos']:
            new_curve_info[curve_info['type']] = curve_info
        level_data['curveInfos'] = new_curve_info

    return temp_list
