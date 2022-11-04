import json


def get_values_from_languages(languages: dict, key_id: str) -> dict:
    values = {}
    for language_key in languages:
        value = languages[language_key].get(key_id, 'None')
        values[language_key] = value

    return values


def get_languages(genshin_data_path: str, language_keys: list[str]) -> dict:
    language_map = {}
    for key in language_keys:
        text_map_path = genshin_data_path + 'TextMap/TextMap' + key.upper() + '.json'  # 'TextMap/TextMapEN.json'
        text_map = json.loads(open(text_map_path, encoding='utf8').read())
        language_map[key] = text_map

    return language_map

