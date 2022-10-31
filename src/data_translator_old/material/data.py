import json

class MaterialData:
    def __init__(self,
                 interaction_title_text_map_hash: int,
                 stack_limit: int,
                 item_use: list,
                 rank_level: int,
                 effect_desc_text_map_hash: int,
                 special_desc_text_map_hash: int,
                 type_desc_text_map_hash: int,
                 effect_icon: int,
                 effect_name: int,
                 satiation_params: list,
                 destroy_rule: str,
                 destroy_return_material: list,
                 destroy_return_material_count: list,
                 id: int,
                 name_text_map_hash: int,
                 desc_text_map_hash: int,
                 icon: str,
                 item_type: str,
                 rank: int,
                 gadget_id: int
                 ):
        self.interaction_title_text_map_hash = interaction_title_text_map_hash
        self.stack_limit = stack_limit
        self.item_use = item_use
        self.rank_level = rank_level
        self.effect_desc_text_map_hash = effect_desc_text_map_hash
        self.special_desc_text_map_hash = special_desc_text_map_hash
        self.type_desc_text_map_hash = type_desc_text_map_hash
        self.effect_icon = effect_icon
        self.effect_name = effect_name
        self.satiation_params = satiation_params
        self.destroy_rule = destroy_rule
        self.destroy_return_material = destroy_return_material
        self.destroy_return_material_count = destroy_return_material_count
        self.id = id
        self.name_text_map_hash = name_text_map_hash
        self.desc_text_map_hash = desc_text_map_hash
        self.icon = icon
        self.item_type = item_type
        self.rank = rank
        self.gadget_id = gadget_id


def return_material_data(origin_file_path):
    temp_json_string = open(origin_file_path).read()
    temp_materials = json.loads(temp_json_string)
    material_data = []
    # create class object
    for item in temp_materials:
        material = MaterialData(
            check_artifact_key(item, 'interactionTitleTextMapHash'),
            check_artifact_key(item, 'stack_limit'),
            check_artifact_key(item, 'itemUse'),
            check_artifact_key(item, 'rankLevel'),
            check_artifact_key(item, 'effectDescTextMapHash'),
            check_artifact_key(item, 'specialDescTextMapHash'),
            check_artifact_key(item, 'typeDescTextMapHash'),
            check_artifact_key(item, 'effectIcon'),
            check_artifact_key(item, 'effectName'),
            check_artifact_key(item, 'satiationParams'),
            check_artifact_key(item, 'destroyRule'),
            check_artifact_key(item, 'destroyReturnMaterial'),
            check_artifact_key(item, 'destroyReturnMaterialCount'),
            check_artifact_key(item, 'id'),
            check_artifact_key(item, 'nameTextMapHash'),
            check_artifact_key(item, 'descTextMapHash'),
            check_artifact_key(item, 'icon'),
            check_artifact_key(item, 'itemType'),
            check_artifact_key(item, 'rank'),
            check_artifact_key(item, 'gadgetId'),
        )
        material_data.append(material)
    return material_data


def check_artifact_key(item, key: str):
    if key in item:
        value = item[key]
    else:
        value = None
    return value
