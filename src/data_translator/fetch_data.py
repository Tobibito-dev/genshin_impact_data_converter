from . import config_data_paths

# from . import data_map
from . import artifact
# from . import character
from . import common
from . import food
from . import material


# from . import weapon


# fetch artifact methods
def artifact_data(genshin_data_path):
    artifact_path = genshin_data_path + config_data_paths.artifact_path
    artifact_data_list = artifact.data.return_artifact_data(artifact_path)
    return artifact_data_list


def artifact_set_data(genshin_data_path):
    artifact_set_path = genshin_data_path + config_data_paths.artifact_set_path
    artifact_set_data_list = artifact.set_data.return_artifact_set_data(artifact_set_path)
    return artifact_set_data_list


def artifact_mainstat_data(genshin_data_path):
    artifact_mainstat_path = genshin_data_path + config_data_paths.artifact_mainstat_path
    artifact_mainstat_data_list = artifact.mainstat_data.return_mainstat_data(artifact_mainstat_path)
    return artifact_mainstat_data_list


def artifact_substat_data(genshin_data_path):
    artifact_substat_path = genshin_data_path + config_data_paths.artifact_substat_path
    artifact_substat_data_list = artifact.substat_data.return_substat_data(artifact_substat_path)
    return artifact_substat_data_list


# fetch character data
def character_data(genshin_data_path):
    pass


def character_curve_data(genshin_data_path):
    pass


def character_promote_data(genshin_data_path):
    pass


def character_fetter_data(genshin_data_path):  # ???
    pass


# Todo: character methods

# fetch common methods
def common_data(genshin_data_path):
    common_data_path = genshin_data_path + config_data_paths.common_path
    common_data_list = common.data.return_common_data(common_data_path)
    return common_data_list


# fetch food methods
def food_data(genshin_data_path):
    food_data_path = genshin_data_path + config_data_paths.food_path
    food_data_list = food.data.return_food_data(food_data_path)
    return food_data_list


# fetch material methods
def material_data(genshin_data_path):
    material_data_path = genshin_data_path + config_data_paths.material_path
    material_data_list = material.data.return_material_data(material_data_path)
    return material_data_list
