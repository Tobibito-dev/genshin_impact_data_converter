from . import util


def translate_data(genshin_data_path):
    # language_keys = ['chs', 'cht', 'de', 'en', 'es', 'fr', 'id', 'jp', 'kr', 'pt', 'ru', 'th', 'vi']
    language_keys = ['en', 'de']
    languages = util.text_map_util.get_languages(genshin_data_path, language_keys)
