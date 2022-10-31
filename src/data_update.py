import data_paths

import data_translator_old
import data_updater


# pull data then convert
def update_data():
    pull_data()
    convert_data()


def pull_data():
    data_updater.pull.check_data(data_paths.genshin_data_path)


def convert_data():
    data_translator_old.translate.translate_data(data_paths.genshin_data_path)


