import json

from .config import genshin_data_path
from .value_handler import get_value
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
            new_key = get_value(key, files)
            converted_data[new_key] = get_value(source, files)
        dump_item(converted_data)
