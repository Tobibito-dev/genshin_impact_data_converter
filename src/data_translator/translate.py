import pprint

from . import util
from . import convert_template

from . import templates


def translate_data(genshin_data_path, language_keys: list[str]):
    languages = util.text_map_util.get_languages(genshin_data_path, language_keys)

    weapon = convert_template.convert_template_data(genshin_data_path, languages, templates.weapon.template)

    jade_spear = weapon['primordial_jade_winged_spear']
    print(jade_spear)
    # pprint.pprint(jade_spear)
