from . import util
from . import convert_template

from . import templates


def translate_data(genshin_data_path, language_keys: list[str]):
    languages = util.text_map_util.get_languages(genshin_data_path, language_keys)

    # print(util.text_map_util.get_values_from_languages(languages, str(160493219)))

    weapon = convert_template.convert_data(genshin_data_path, languages, templates.weapon.template)
    print(weapon['primordial_jade_winged_spear'])
