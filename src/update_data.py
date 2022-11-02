import config

import data_translator
# import data_updater


# pull data then convert
def update_data():
    pull_data()
    convert_data()


def pull_data():
    # data_updater.pull.check_data(config.genshin_data_path)
    pass


def convert_data():
    data_translator.translate.translate_data(config.genshin_data_path)


convert_data()
