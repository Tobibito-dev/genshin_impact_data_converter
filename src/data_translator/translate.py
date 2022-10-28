# import json

from . import config_data_paths
from . import text_map_util

# from . import data_map
from . import artifact
# from . import character
from . import common
from . import food
from . import material


# from . import weapon


def translate_data(genshin_data_path):
    # load languages
    languages = text_map_util.get_languages(genshin_data_path)

    # artifact data
    artifact_data = fetch_artifact_data(genshin_data_path)
    artifact_set_data = fetch_artifact_set_data(genshin_data_path)
    artifact_mainstat_data = fetch_artifact_mainstat_data(genshin_data_path)
    artifact_substat_data = fetch_artifact_substat_data(genshin_data_path)

    # character data

    # common data
    common_data = fetch_common_data(genshin_data_path)

    # food data
    food_data = fetch_food_data(genshin_data_path)

    # material data
    material_data = fetch_material_data(genshin_data_path)

    # weapon data

    # test data
    # print(text_map_util.get_value_from_language(languages['en'], str(artifact_data[3000].name_text_hash_map)))


# fetch artifact methods
def fetch_artifact_data(genshin_data_path):
    artifact_path = genshin_data_path + config_data_paths.artifact_path
    artifact_data_list = artifact.data.return_artifact_data(artifact_path)
    return artifact_data_list


def fetch_artifact_set_data(genshin_data_path):
    artifact_set_path = genshin_data_path + config_data_paths.artifact_set_path
    artifact_set_data_list = artifact.set_data.return_artifact_set_data(artifact_set_path)
    return artifact_set_data_list


def fetch_artifact_mainstat_data(genshin_data_path):
    artifact_mainstat_path = genshin_data_path + config_data_paths.artifact_mainstat_path
    artifact_mainstat_data_list = artifact.mainstat_data.return_mainstat_data(artifact_mainstat_path)
    return artifact_mainstat_data_list


def fetch_artifact_substat_data(genshin_data_path):
    artifact_substat_path = genshin_data_path + config_data_paths.artifact_substat_path
    artifact_substat_data_list = artifact.substat_data.return_substat_data(artifact_substat_path)
    return artifact_substat_data_list


# fetch common methods
def fetch_common_data(genshin_data_path):
    common_data_path = genshin_data_path + config_data_paths.common_path
    common_data_list = common.data.return_common_data(common_data_path)
    return common_data_list


# fetch food methods
def fetch_food_data(genshin_data_path):
    food_data_path = genshin_data_path + config_data_paths.food_path
    food_data_list = food.data.return_food_data(food_data_path)
    return food_data_list


# fetch material methods
def fetch_material_data(genshin_data_path):
    material_data_path = genshin_data_path + config_data_paths.material_path
    material_data_list = material.data.return_material_data(material_data_path)
    return material_data_list
