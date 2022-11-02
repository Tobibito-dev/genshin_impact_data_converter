import json

from .. import config_data_paths


def food_data(genshin_data_path):
    temp_list = json.loads(open(genshin_data_path + config_data_paths.food_path).read())
    return temp_list
