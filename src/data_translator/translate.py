import pprint

from . import util
from . import convert_template

from . import templates


def translate_data(genshin_data_path, language_keys: list[str]):
    languages = util.text_map_util.get_languages(genshin_data_path, language_keys)

    food = convert_template.convert_template_data(genshin_data_path, languages, templates.food.template)

    weapon = convert_template.convert_template_data(genshin_data_path, languages, templates.weapon.template)

    jade_spear = weapon['primordial_jade_winged_spear']
    pprint.pprint(jade_spear)

    # pprint.pprint(food['adeptus_temptation'])
