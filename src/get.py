from . import data_manager


def get_character(char_key: str):
    character = data_manager.get.object_data('characters', char_key)
    return character
