class CookRecipeExcelConfigData:  # ex. adeptus temptation
    def __init__(self,
                 id: int,
                 name_text_map_hash: int,
                 rank_level: int,
                 icon: str,
                 desc_text_map_hash: int,
                 effect_desc: list,
                 max_proficiency: int,
                 quality_output_vec: list[dict],
                 input_vec: list[dict],
                 qte_param: str,
                 qte_quality_weight_vec: list[int]):
        self.id = id  # 5101
        self.name_text_map_hash = name_text_map_hash  # 2535717720
        self.rank_level = rank_level  # 5
        self.icon = icon  # "UI_ItemIcon_108123"
        self.desc_text_hash_map = desc_text_map_hash  # 3785660866
        self.effect_desc = effect_desc  # [1022833117, 3090219849, 3779451422, 4255144839]
        self.food_type = "COOK_FOOD_ATTACK"
        self.cook_method = "COOK_METHOD_BOIL"
        self.max_proficiency = max_proficiency  # 25
        self.quality_output_vec = quality_output_vec
        self.input_vec = input_vec
        self.qte_param = qte_param
        self.qte_quality_weight_vec = qte_quality_weight_vec

def return_recipe_excel_config_data(origin_file_path):
    print(origin_file_path)
    cook_recipe_excel_config_data = []
    return cook_recipe_excel_config_data
