# food path
food_path = 'ExcelBinOutput/CookRecipeExcelConfigData.json'

template = {
    'type': 'food',
    'paths': {'main': food_path},
    'data': {'name': {'path': 'main', 'key': 'nameTextMapHash', 'conversionMethod': 'textMap'},
             'id': {'path': 'main', 'key': 'id', 'conversionMethod': 'direct'},
             'foodType': {'path': 'main', 'key': 'foodType', 'conversionMethod': 'direct'},
             'cookMethod': {'path': 'main', 'key': 'cookMethod', 'conversionMethod': 'direct'},
             'rankLevel': {'path': 'main', 'key': 'rankLevel', 'conversionMethod': 'direct'},
             'isDefaultUnlocked': {'path': 'main', 'key': 'isDefaultUnlocked', 'conversionMethod': 'direct'},
             'maxProficiency': {'path': 'main', 'key': 'maxProficiency', 'conversionMethod': 'direct'},
             'inputVec': {'path': 'main', 'key': 'inputVec', 'conversionMethod': 'direct'},
             'qualityOutputVec': {'path': 'main', 'key': 'qualityOutputVec', 'conversionMethod': 'direct'},
             'qteParam': {'path': 'main', 'key': 'qteParam', 'conversionMethod': 'direct'},
             'qteQualityWeightVec': {'path': 'main', 'key': 'qteQualityWeightVec', 'conversionMethod': 'direct'},
             'effectDesc': {'path': 'main', 'key': 'effectDesc', 'conversionMethod': 'textMap'}
             }
}
