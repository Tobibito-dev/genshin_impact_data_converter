import json

from .config import genshin_data_path, language_keys

languages = {}

def get_values_from_languages(key_id: str) -> dict:
    values = {}
    for language_key in languages:
        value = languages[language_key].get(key_id, 'None')
        values[language_key] = value

    return values


def get_languages() -> dict:
    language_map = {}
    for key in language_keys:
        text_map_path = genshin_data_path + 'TextMap/TextMap' + key.upper() + '.json'  # 'TextMap/TextMapEN.json'
        with open(text_map_path, encoding='utf8') as text_map_file:
            text_map = json.loads(text_map_file.read())
            language_map[key] = text_map

    return language_map

def init_languages():
    global languages
    languages = get_languages()