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

    def get_stats(self, level: int, promoted=False):
        stats = []
        promote_stats = []
        if not hasattr(self, 'curve'):
            print('no curve existing')
            stats = None
        elif level < 1 or level > 100:
            print('this level doesnt exist')
            stats = None
        else:
            for index, base_stat in enumerate(getattr(self, 'baseStats')):
                stat = {}
                curve_stat = getattr(self, 'curve')[level][index]
                stat['type'] = base_stat['type']
                stat['value'] = float_calculator.calculate(base_stat['value'], curve_stat['value'], curve_stat['arith'])
                stats.append(stat)

            for promote in getattr(self, 'promote'):
                promote_max_level = promote['unlockMaxLevel']
                if not promoted and level <= promote_max_level:
                    promote_stats = promote['addProps']
                    break
                elif promoted and level < promote_max_level:
                    promote_stats = promote['addProps']
                    break
                elif level == 90 and promote_max_level == 90:
                    promote_stats = promote['addProps']
                    break

            for promote_stat in promote_stats:
                if 'value' in promote_stat:
                    promote_stat_type = promote_stat['propType']
                    promote_stat_value = promote_stat['value']
                    stat_found = False
                    for stat in stats:
                        if stat['type'] == promote_stat_type:
                            stat['value'] = float_calculator.calculate(stat['value'], promote_stat_value, 'ARITH_ADD')
                            stat_found = True
                            break
                    if not stat_found:
                        stats.append(promote_stat)

        return stats
