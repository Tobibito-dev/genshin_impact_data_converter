from . import config_data_paths

from . import food
from . import artifact


def translate_data(genshin_data_path):
    # artifact data

    # single piece
    artifact_path = genshin_data_path + config_data_paths.artifact_path
    artifact_data_list = \
        artifact.data.return_artifact_data(artifact_path)

    # set
    artifact_set_path = genshin_data_path + config_data_paths.artifact_set_path
    artifact_set_data_list = \
        artifact.set_data.return_artifact_set_data(artifact_set_path)

    # artifact main stats



    # food data
    food_recipe_path = genshin_data_path + config_data_paths.food_recipe_path
    food_recipe_list = food.recipe_data.return_food_recipe_data(food_recipe_path)
