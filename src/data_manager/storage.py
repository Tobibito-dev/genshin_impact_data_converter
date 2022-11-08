from .util import float_calculator

data = {}


def replace_data(new_data: dict):
    global data
    for cat_key in new_data:
        data[cat_key] = {}
        for item_key in new_data[cat_key]:
            data[cat_key][item_key] = DataObject(new_data[cat_key][item_key])


class DataObject:
    def __init__(self, object_data: dict):
        self.data = object_data
        if type(object_data) != int:
            for key in object_data:
                setattr(self, key, object_data[key])

    def get_value(self, key: str):
        value = getattr(self, key)
        return value

    def get_stats(self, level: int):
        if not hasattr(self, 'curve'):
            print('no curve existing')
            stats = None
        elif level < 1 or level > 100:
            print('this level doesnt exist')
            stats = None
        else:
            stats = []
            for base_stat in getattr(self, 'baseStats'):
                stats.append(base_stat)
            for index, stat in enumerate(stats):
                curve_stat = getattr(self, 'curve')[level][index]
                stat['value'] = float_calculator.calculate(stat['value'], curve_stat['value'], curve_stat['arith'])
        return stats
