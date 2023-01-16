import json

from threading import Thread

from tqdm import tqdm

from .config import genshin_data_path
from .value_handler import get_key_value_pair
from .file_handler import dump_item


def convert_to_template(template, paths):
    files = {}
    for path in paths:
        full_path = genshin_data_path + paths[path]
        with open(full_path, 'r', encoding='utf8') as json_file:
            files[path] = json.loads(json_file.read())

    for entry in tqdm(files['codex'], position=0, leave=True, desc=template['templateType'], ncols=100):
        files['entry'] = entry
        entry_converter = Thread(target=convert_entry_to_template, args=(template, files))
        entry_converter.start()

    return

def convert_entry_to_template(template, files):
    converted_data = {}
    for key in template:
        source = template[key]
        key_value_pair = get_key_value_pair(key, source, files)
        converted_data[key_value_pair[0]] = key_value_pair[1]
    dump_item(converted_data)
    return
