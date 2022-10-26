import json


# TODO: assign file objects for json

def get_value_from_language(genshin_data_path, language_key: str, key_id: str):
    languages = get_languages(genshin_data_path)
    language = languages[language_key]
    language_json = json.loads(language.read())
    value = language_json[key_id]
    return value




def get_languages(genshin_data_path):
    text_map_chs = open(genshin_data_path + 'TextMap/TextMapCHS.json', encoding='utf8')
    text_map_cht = open(genshin_data_path + 'TextMap/TextMapCHT.json', encoding='utf8')
    text_map_de = open(genshin_data_path + 'TextMap/TextMapDE.json', encoding='utf8')
    text_map_en = open(genshin_data_path + 'TextMap/TextMapEN.json', encoding='utf8')
    text_map_es = open(genshin_data_path + 'TextMap/TextMapES.json', encoding='utf8')
    text_map_fr = open(genshin_data_path + 'TextMap/TextMapFR.json', encoding='utf8')
    text_map_id = open(genshin_data_path + 'TextMap/TextMapID.json', encoding='utf8')
    text_map_jp = open(genshin_data_path + 'TextMap/TextMapJP.json', encoding='utf8')
    text_map_kr = open(genshin_data_path + 'TextMap/TextMapKR.json', encoding='utf8')
    text_map_pt = open(genshin_data_path + 'TextMap/TextMapPT.json', encoding='utf8')
    text_map_ru = open(genshin_data_path + 'TextMap/TextMapRU.json', encoding='utf8')
    text_map_th = open(genshin_data_path + 'TextMap/TextMapTH.json', encoding='utf8')
    text_map_vi = open(genshin_data_path + 'TextMap/TextMapVI.json', encoding='utf8')

    language_map = {
        "chs": text_map_chs,
        "cht": text_map_cht,
        "de": text_map_de,
        "en": text_map_en,
        "es": text_map_es,
        "fr": text_map_fr,
        "id": text_map_id,
        "jp": text_map_jp,
        "kr": text_map_kr,
        "pt": text_map_pt,
        "ru": text_map_ru,
        "th": text_map_th,
        "vi": text_map_vi
    }
    return language_map


def name_to_key(name: str):
    # TODO: name to key
    pass
