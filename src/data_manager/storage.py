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
