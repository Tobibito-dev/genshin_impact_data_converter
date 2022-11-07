from .util import text_map_util
from . import convert_template

from . import templates


def translate_data(genshin_data_path, language_keys: list[str]):
    languages = text_map_util.get_languages(genshin_data_path, language_keys)

    translated_data = {
        'artifact': convert_template.convert_template_data(genshin_data_path, languages, templates.artifact.template),
        'character': convert_template.convert_template_data(genshin_data_path, languages, templates.character.template),
        'common': convert_template.convert_template_data(genshin_data_path, languages, templates.common.template),
        'food': convert_template.convert_template_data(genshin_data_path, languages, templates.food.template),
        'material': convert_template.convert_template_data(genshin_data_path, languages, templates.material.template),
        'weapon': convert_template.convert_template_data(genshin_data_path, languages, templates.weapon.template)
    }

    return translated_data

