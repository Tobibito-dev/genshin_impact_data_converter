from .util import text_map_util
from . import food, weapon


def translate_data(genshin_data_path: str):
    print('Getting Languages')
    languages = text_map_util.get_languages(genshin_data_path)

    print('Starting translation')
    foods = food.data.get(genshin_data_path, languages['en'])
    weapons = weapon.data.get_weapons(genshin_data_path, languages['en'])
