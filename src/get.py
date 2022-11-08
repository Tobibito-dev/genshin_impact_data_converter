from . import data_manager
from .data_manager.storage import DataObject


def get_all_data():
    return data_manager.get.all_data()


def get_object(cat_key: str, char_key: str) -> DataObject:
    character = data_manager.get.data_object(cat_key, char_key)
    return character


def get_category(cat_key: str):
    category = data_manager.get.category(cat_key)
    return category
