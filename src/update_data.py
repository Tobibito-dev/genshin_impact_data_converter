from . import config

from .data_manager import storage

from . import data_translator
# from . import data_updater


# pull data then convert
def update_data():
    pull_data()
    convert_data()


def pull_data():
    # data_updater.pull.check_data(config.genshin_data_path)
    pass


def convert_data():
    storage.replace_data(data_translator.translate.translate_data(config.genshin_data_path, config.language_keys))
