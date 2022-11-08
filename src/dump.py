from . import config

from . import data_manager


def dump_all(one_file=False):
    data_manager.dump.all_data(config.dump_data_path, one_file)
