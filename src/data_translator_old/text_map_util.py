import json


def get_value_from_language(language, key_id: str):
    if key_id in language:
        value = language[key_id]
    else:
        value = None
    return value


def get_languages(genshin_data_path):
    # create json object of each language
    # will be closed later
    # fasted method unfortunately
    # high flexibility
    text_map_chs = json.loads(open(genshin_data_path + 'TextMap/TextMapCHS.json', encoding='utf8').read())
    text_map_cht = json.loads(open(genshin_data_path + 'TextMap/TextMapCHT.json', encoding='utf8').read())
    text_map_de = json.loads(open(genshin_data_path + 'TextMap/TextMapDE.json', encoding='utf8').read())
    text_map_en = json.loads(open(genshin_data_path + 'TextMap/TextMapEN.json', encoding='utf8').read())
    text_map_es = json.loads(open(genshin_data_path + 'TextMap/TextMapES.json', encoding='utf8').read())
    text_map_fr = json.loads(open(genshin_data_path + 'TextMap/TextMapFR.json', encoding='utf8').read())
    text_map_id = json.loads(open(genshin_data_path + 'TextMap/TextMapID.json', encoding='utf8').read())
    text_map_jp = json.loads(open(genshin_data_path + 'TextMap/TextMapJP.json', encoding='utf8').read())
    text_map_kr = json.loads(open(genshin_data_path + 'TextMap/TextMapKR.json', encoding='utf8').read())
    text_map_pt = json.loads(open(genshin_data_path + 'TextMap/TextMapPT.json', encoding='utf8').read())
    text_map_ru = json.loads(open(genshin_data_path + 'TextMap/TextMapRU.json', encoding='utf8').read())
    text_map_th = json.loads(open(genshin_data_path + 'TextMap/TextMapTH.json', encoding='utf8').read())
    text_map_vi = json.loads(open(genshin_data_path + 'TextMap/TextMapVI.json', encoding='utf8').read())

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
