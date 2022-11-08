from . import config

from . import data_manager


def dump_all():
    data_manager.dump.all_data(config.dump_data_path)
