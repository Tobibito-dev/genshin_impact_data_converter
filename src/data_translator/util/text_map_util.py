import json


def get_values_from_languages(languages: dict, key_id: str):
    values = {}
    for language_key in languages['keys']:
        if key_id in languages['values'][language_key]:
            value = languages['values'][language_key][key_id]
        else:
            value = None
        values[language_key] = value
    return values


def get_languages(genshin_data_path: str, language_keys: list[str]):
    language_values = {}
    for key in language_keys:
        path = genshin_data_path + 'TextMap/TextMap' + key.upper() + '.json'  # 'TextMap/TextMapEN.json'
        text_map = json.loads(open(path, encoding='utf8').read())
        language_values[key] = text_map

    language_map = {'keys': language_keys,
                    'values': language_values}
    return language_map


