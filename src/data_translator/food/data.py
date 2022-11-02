from . import prepare_data

from .. import util


def get(genshin_data_path: str, language):
    print('Translating food')
    food = {}
    food_data = prepare_data.food_data(genshin_data_path)
    unknown = 0
    for item in food_data:
        name = util.text_map_util.get_value_from_language(language, str(item['nameTextMapHash']))
        key = str(name).lower().replace(' ', '_').replace("'", '')
        if key == 'none':
            key = 'unknown' + str(unknown)
            unknown = unknown + 1

        food[key] = {'foodName': name,
                     'foodText': 'desc',
                     }

    food['unknownCount'] = unknown
    print(food['universal_peace'])

    return food
