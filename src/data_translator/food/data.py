import json


class FoodRecipe:  # ex. adeptus temptation
    def __init__(self,
                 id: int,
                 name_text_map_hash: int,
                 rank_level: int,
                 icon: str,
                 desc_text_map_hash: int,
                 effect_desc: list,
                 food_type: str,
                 cook_method: str,
                 max_proficiency: int,
                 quality_output_vec: list[dict],
                 input_vec: list[dict],
                 qte_param: str,
                 qte_quality_weight_vec: list[int]
                 ):
        self.id = id  # 5101
        self.name_text_map_hash = name_text_map_hash  # 2535717720
        self.rank_level = rank_level  # 5
        self.icon = icon  # "UI_ItemIcon_108123"
        self.desc_text_hash_map = desc_text_map_hash  # 3785660866
        self.effect_desc = effect_desc  # [1022833117, 3090219849, 3779451422, 4255144839]
        self.food_type = food_type
        self.cook_method = cook_method
        self.max_proficiency = max_proficiency  # 25
        self.quality_output_vec = quality_output_vec
        self.input_vec = input_vec
        self.qte_param = qte_param
        self.qte_quality_weight_vec = qte_quality_weight_vec


def return_food_data(origin_file_path):
    temp_json_string = open(origin_file_path).read()
    temp_recipes = json.loads(temp_json_string)
    food_recipe_data = []
    for item in temp_recipes:
        food = FoodRecipe(
            check_food_key(item, 'id'),
            check_food_key(item, 'nameTextMapHash'),
            check_food_key(item, 'rankLevel'),
            check_food_key(item, 'icon'),
            check_food_key(item, 'descTextMapHash'),
            check_food_key(item, 'effectDesc'),
            check_food_key(item, 'foodType'),
            check_food_key(item, 'cookMethod'),
            check_food_key(item, 'maxProficiency'),
            check_food_key(item, 'qualityOutputVec'),
            check_food_key(item, 'inputVec'),
            check_food_key(item, 'qteParam'),
            check_food_key(item, 'qteQualityWeightVec'),
        )
        food_recipe_data.append(food)
    return food_recipe_data


def check_food_key(item, key: str):
    if key in item:
        value = item[key]
    else:
        value = None
    return value
