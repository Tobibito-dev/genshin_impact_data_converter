from . import util


def translate_data(genshin_data_path, language_keys: list[str]):
    languages = util.text_map_util.get_languages(genshin_data_path, language_keys)

    print(util.text_map_util.get_value_from_languages(languages, str(2410593283)))
