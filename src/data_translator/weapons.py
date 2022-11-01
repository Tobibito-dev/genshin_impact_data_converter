import json

from . import config_data_paths


def get_weapons(genshin_data_path):
    weapon_data = json.loads(open(genshin_data_path + config_data_paths.weapon_path).read())
    weapon_promote_data = json.loads(open(genshin_data_path + config_data_paths.weapon_promote_path).read())
    weapon_curve_data = json.loads(open(genshin_data_path + config_data_paths.weapon_curve_path).read())
