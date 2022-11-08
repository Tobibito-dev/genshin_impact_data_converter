from . import storage


def all_data():
    return storage.data


def category(cat_key: str):
    return storage.data.get(cat_key)


def data_object(cat_key, obj_key: str):
    if cat_key in storage.data and obj_key in storage.data[cat_key]:
        obj_data = storage.data[cat_key][obj_key]
    else:
        print("key doesn't exist")
        obj_data = None
    return obj_data
