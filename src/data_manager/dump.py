import json

from pathlib import Path

from . import storage


def all_data(dump_data_path: str, one_file=False):
    if not one_file:
        for data_type in storage.data:
            type_dump_path = dump_data_path + data_type + '/'
            Path(type_dump_path).mkdir(parents=True, exist_ok=True)

            for item_key in storage.data[data_type]:
                item_dump_path = type_dump_path + item_key + '.json'
                item_data = storage.data[data_type][item_key]

                with open(item_dump_path, 'w', encoding='utf8') as item_file:
                    json.dump(item_data.data, item_file, indent=4, ensure_ascii=False)

    else:
        Path(dump_data_path).mkdir(exist_ok=True)
        file_path = dump_data_path + 'data.json'
        all_data_dict = {}

        for data_type in storage.data:
            all_data_dict[data_type] = {}
            for item_key in storage.data[data_type]:
                all_data_dict[data_type][item_key] = storage.data[data_type][item_key].data

        with open(file_path, 'w', encoding='utf8') as data_file:
            json.dump(all_data_dict, data_file, indent=4, ensure_ascii=False)
