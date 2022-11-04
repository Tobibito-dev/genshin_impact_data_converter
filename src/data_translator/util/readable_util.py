import os


def get_readable_data(genshin_data_path: str, languages: dict, key_id: str, item_type: str):
    values = {}
    for language_key in languages:
        dir_key = language_key.upper()
        readable_path = \
            genshin_data_path + 'Readable/' + dir_key + '/' + item_type.capitalize() + key_id + '_' + dir_key + '.txt'
        if os.path.isfile(readable_path):
            with open(readable_path, 'r', encoding='utf8') as temp_readable:
                values[language_key] = temp_readable.read()
        else:
            values[language_key] = None

    return values
