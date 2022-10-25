# TODO: assign file objects for json

text_map_chs = open('../GenshinData/TextMap/TextMapCHS.json')
text_map_cht = open('../GenshinData/TextMap/TextMapCHT.json')
text_map_de = open('../GenshinData/TextMap/TextMapDE.json')
text_map_en = open('../GenshinData/TextMap/TextMapEN.json')
text_map_es = open('../GenshinData/TextMap/TextMapES.json')
text_map_fr = open('../GenshinData/TextMap/TextMapFR.json')
text_map_id = open('../GenshinData/TextMap/TextMapID.json')
text_map_jp = open('../GenshinData/TextMap/TextMapJP.json')
text_map_kr = open('../GenshinData/TextMap/TextMapKR.json')
text_map_pt = open('../GenshinData/TextMap/TextMapPT.json')
text_map_ru = open('../GenshinData/TextMap/TextMapRU.json')
text_map_th = open('../GenshinData/TextMap/TextMapTH.json')
text_map_vi = open('../GenshinData/TextMap/TextMapVI.json')

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

def name_to_key(name: str):
    #TODO: name to key
    pass
