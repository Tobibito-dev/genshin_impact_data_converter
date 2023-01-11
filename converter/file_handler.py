import json
import shutil
from pathlib import Path

from .config import dump_data_path

def dump_item(item):
    type_dump_path = dump_data_path + item['templateType'] + '/'
    Path(type_dump_path).mkdir(parents=True, exist_ok=True)
    item_key = item['name']['en'].replace("'", '').title()
    chars = ['"', '.', '?', '!', '#', ' ', '-', ':']
    for char in chars:
        item_key = item_key.replace(char, '')
    item_dump_path = type_dump_path + item_key + '.json'

    with open(item_dump_path, 'w', encoding='utf8') as item_file:
        json.dump(item, item_file, indent=4, ensure_ascii=False)


def reset_output():
    if Path(dump_data_path).exists():
        shutil.rmtree(dump_data_path)