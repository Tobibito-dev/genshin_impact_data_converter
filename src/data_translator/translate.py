# import json

from . import fetch_data
from . import text_map_util







def translate_data(genshin_data_path):
    # load languages
    languages = text_map_util.get_languages(genshin_data_path)

    # artifact data
    artifact_data = fetch_data.artifact_data(genshin_data_path)
    artifact_set_data = fetch_data.artifact_set_data(genshin_data_path)
    artifact_mainstat_data = fetch_data.artifact_mainstat_data(genshin_data_path)
    artifact_substat_data = fetch_data.artifact_substat_data(genshin_data_path)

    # character data

    # common data
    common_data = fetch_data.common_data(genshin_data_path)

    # food data
    food_data = fetch_data.food_data(genshin_data_path)

    # material data
    material_data = fetch_data.material_data(genshin_data_path)

    # weapon data

    # test data
    # print(text_map_util.get_value_from_language(languages['en'], str(artifact_data[3000].name_text_hash_map)))


