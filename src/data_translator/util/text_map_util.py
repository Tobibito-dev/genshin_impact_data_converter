import json


def get_value_from_language(language, key_id: str):
    if key_id in language:
        value = language[key_id]
    else:
        value = None
    return value


def get_languages(genshin_data_path: str, language_keys: list[str]):
    language_map = {}
    for key in language_keys:
        path = genshin_data_path + 'TextMap/TextMap' + key.upper() + '.json'  # 'TextMap/TextMapEN.json'
        text_map = json.loads(open(path, encoding='utf8').read())
        language_map[key] = text_map

    return language_map


