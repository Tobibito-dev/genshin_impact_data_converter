import json


class ArtifactSetData:
    def __init__(self,
                 set_id: int,
                 set_icon: str,
                 set_need_num: list[int],
                 equip_affix_id: int,
                 contains_list: list[int],
                 text_list: list[int]
                 ):
        self.set_id = set_id
        self.set_icon = set_icon
        self.set_need_num = set_need_num
        self.equip_affix_id = equip_affix_id
        self.contains_list = contains_list
        self.text_list = text_list


def return_artifact_set_data(origin_file_path):
    temp_json_string = open(origin_file_path).read()
    temp_reliq_sets = json.loads(temp_json_string)
    artifact_set_data = []
    for item in temp_reliq_sets:
        artifact_set = ArtifactSetData (
            check_artifact_set_key(item, 'setId'),
            check_artifact_set_key(item, 'setIcon'),
            check_artifact_set_key(item, 'setNeedNum'),
            check_artifact_set_key(item, 'EquipAffixId'),
            check_artifact_set_key(item, 'containsList'),
            # FDKHPHNGCBL no idea
            # JCLGCACJMMK no idea
            check_artifact_set_key(item, 'textList')
        )
        artifact_set_data.append(artifact_set)
    return artifact_set_data


def check_artifact_set_key(item, key: str):
    if key in item:
        value = item[key]
    else:
        value = None
    return value
