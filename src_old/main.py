from . import config

from .data_manager import storage

from .data_translator.translate import translate_data
from . import data_updater


# pull data then convert
# change pre_release on your own risk
def init(pre_release=False):
    # pull_data()
    convert_data(pre_release=pre_release)


def pull_data():
    data_updater.pull.check_data(config.genshin_data_path)


def convert_data(pre_release=False):
    storage.replace_data(translate_data(config.genshin_data_path, config.language_keys, pre_release=pre_release))
