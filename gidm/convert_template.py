import json
from pathlib import Path

from .config import genshin_data_path, dump_data_path
from .value_handler import get_value

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
            value_found = False
            source = template[key]
            converted_data[key] = get_value(source, files)
        print(converted_data)
        dump_item(converted_data)

def dump_item(item):
    type_dump_path = dump_data_path + item['templateType'] + '/'
    Path(type_dump_path).mkdir(parents=True, exist_ok=True)
    item_key = item['name']['en'].title()
    chars = ['"', '.', '?', '!', '#', ' ', '-', ':', "'"]
    for char in chars:
        item_key = item_key.replace(char, '')
    item_dump_path = type_dump_path + item_key + '.json'

    with open(item_dump_path, 'w', encoding='utf8') as item_file:
        json.dump(item, item_file, indent=4, ensure_ascii=False)
