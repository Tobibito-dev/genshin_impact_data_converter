import json


class ArtifactData:
    def __init__(self,
                 equip_type: str,  # add DArtifact slot key
                 show_pic: str,
                 rank_level: int,
                 main_prop_depot_id: int,
                 append_prop_depot_id: int,
                 set_id: int,
                 add_prop_levels: list[int],
                 base_conv_exp: int,
                 max_level: int,
                 story_id: int,
                 destroy_return_material: list[int],
                 destroy_return_material_count: list[int],
                 id: int,
                 name_text_map_hash: int,
                 desc_text_map_hash: int,
                 icon: str,
                 item_type: str,
                 weight: int,
                 rank: int,
                 gadget_id: int
                 ):
        self.equip_type = equip_type
        self.show_pic = show_pic
        self.rank_level = rank_level
        self.main_prop_depot_id = main_prop_depot_id
        self.append_prop_depot_id = append_prop_depot_id
        self.set_id = set_id
        self.add_prop_levels = add_prop_levels
        self.base_conv_exp = base_conv_exp
        self.max_level = max_level
        self.story_id = story_id
        self.destroy_rule = "DESTROY_RETURN_MATERIAL"
        self.destroy_return_material = destroy_return_material
        self.destroy_return_material_count = destroy_return_material_count
        self.id = id
        self.name_text_hash_map = name_text_map_hash
        self.desc_text_map_hash = desc_text_map_hash
        self.icon = icon
        self.item_type = item_type
        self.weight = weight
        self.rank = rank
        self.gadget_id = gadget_id


def return_artifact_data(origin_file_path):
    temp_json_string = open(origin_file_path).read()
    temp_artifacts = json.loads(temp_json_string)
    artifact_data = []
    # create class object
    for item in temp_artifacts:
        artifact = ArtifactData(
            check_artifact_key(item, 'equipType'),
            check_artifact_key(item, 'showPic'),
            check_artifact_key(item, 'rankLevel'),
            check_artifact_key(item, 'mainPropDepotId'),
            check_artifact_key(item, 'appendPropDepotId'),
            check_artifact_key(item, 'setId'),
            check_artifact_key(item, 'addPropLevels'),
            check_artifact_key(item, 'baseConvExp'),
            check_artifact_key(item, 'maxLevel'),
            check_artifact_key(item, 'storyId'),
            check_artifact_key(item, 'destroyReturnMaterial'),
            check_artifact_key(item, 'destroyReturnMaterialCount'),
            check_artifact_key(item, 'id'),
            check_artifact_key(item, 'nameTextMapHash'),
            check_artifact_key(item, 'descTextMapHash'),
            check_artifact_key(item, 'icon'),
            check_artifact_key(item, 'itemType'),
            check_artifact_key(item, 'weight'),
            check_artifact_key(item, 'rank'),
            check_artifact_key(item, 'gadgetId'),
        )
        artifact_data.append(artifact)
    return artifact_data


def check_artifact_key(item, key: str):
    if key in item:
        value = item[key]
    else:
        value = None
    return value
