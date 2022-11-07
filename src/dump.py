from . import config

from .data_manager import dump


def dump_all():
    dump.dump_all(config.dump_data_path)
