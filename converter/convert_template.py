import json

from .config import genshin_data_path
from .value_handler import get_key_value_pair
from .file_handler import dump_item


def convert_to_template(template, paths):
    files = {}
    for path in paths:
        full_path = genshin_data_path + paths[path]
        with open(full_path, 'r', encoding='utf8') as json_file:
            files[path] = json.loads(json_file.read())

    for entry in files['codex']:
        files['entry'] = entry
        converted_data = {}
        for key in template:
            source = template[key]
            key_value_pair = get_key_value_pair(key, source, files)
            print(key_value_pair)
            converted_data[key_value_pair[0]] = key_value_pair[1]
        dump_item(converted_data)
