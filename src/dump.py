from . import config

from . import data_manager


def dump_all(one_file=False, reset_dir=True):
    data_manager.dump.all_data(config.dump_data_path, one_file, reset_dir)
