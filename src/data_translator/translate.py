from . import weapons


def translate_data(genshin_data_path):
    weapons.get_weapons(genshin_data_path)
