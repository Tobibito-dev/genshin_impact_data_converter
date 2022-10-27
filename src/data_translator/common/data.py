import json


class CommonData:
    def __init__(self,
                 affix_id: int,
                 id: int,
                 level: int,
                 name_text_map_hash: int,
                 desc_text_map_hash: int,
                 open_config: str,
                 add_props: list,
                 param_list: list[int]
                 ):
        self.affix_id = affix_id
        self.id = id
        self.level = level
        self.name_text_map_hash = name_text_map_hash
        self.desc_text_map_hash = desc_text_map_hash
        self.open_config = open_config
        self.add_props = add_props
        self.param_list = param_list


def return_common_data(origin_file_path):
    temp_json_string = open(origin_file_path).read()
    temp_commons = json.loads(temp_json_string)
    common_data = []
    # create class object
    for item in temp_commons:
        common = CommonData(
            check_common_key(item, 'affixId'),
            check_common_key(item, 'id'),
            check_common_key(item, 'level'),
            check_common_key(item, 'nameTextMapHash'),
            check_common_key(item, 'descTextMapHash'),
            check_common_key(item, 'openConfig'),
            check_common_key(item, 'addProps'),
            check_common_key(item, 'paramList'),
        )
        common_data.append(common)
    return common_data


def check_common_key(item, key: str):
    if key in item:
        value = item[key]
    else:
        value = None
    return value
