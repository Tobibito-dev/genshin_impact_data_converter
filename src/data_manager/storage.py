from .util import float_calculator
from .data_object import DataObject

data = {}


def replace_data(new_data: dict):
    global data
    for cat_key in new_data:
        data[cat_key] = {}
        for item_key in new_data[cat_key]:
            data[cat_key][item_key] = DataObject(new_data[cat_key][item_key])
