from . import config_data_paths

from . import food


def translate_data(genshin_data_path):
    cook_recipe_path = genshin_data_path + config_data_paths.cook_recipe_excel_config_data_path
    food.cook_recipe_excel_config_data.return_recipe_excel_config_data(cook_recipe_path)
