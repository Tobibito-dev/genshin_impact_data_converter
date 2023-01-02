from .util import text_map_util
from .convert_template import convert_template_data

from . import templates


def translate_data(genshin_data_path, language_keys: list[str], pre_release=False):
    languages = text_map_util.get_languages(genshin_data_path, language_keys)

    translated_data = {
        'artifacts': convert_template_data(genshin_data_path, languages, templates.artifact.template, pre_release),
        'characters': convert_template_data(genshin_data_path, languages, templates.character.template, pre_release),
        'common': convert_template_data(genshin_data_path, languages, templates.common.template, pre_release),
        'food': convert_template_data(genshin_data_path, languages, templates.food.template, pre_release),
        'materials': convert_template_data(genshin_data_path, languages, templates.material.template, pre_release),
        'weapons': convert_template_data(genshin_data_path, languages, templates.weapon.template, pre_release)
    }

    return translated_data

