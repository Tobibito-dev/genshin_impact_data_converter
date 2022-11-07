import json

from pathlib import Path

from . import data


def dump_all(dump_data_path):
    for data_type in data.data_obj:
        type_dump_path = dump_data_path + data_type + '/'
        Path(type_dump_path).mkdir(parents=True, exist_ok=True)

        for item in data.data_obj[data_type]:
            item_dump_path = type_dump_path + item + '.json'
            item_data = data.data_obj[data_type][item]

            with open(item_dump_path, 'w') as item_file:
                json.dump(item_data, item_file, indent=4, ensure_ascii=False)
