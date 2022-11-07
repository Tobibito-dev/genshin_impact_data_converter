from . import update_data
from . import config

from .data_manager import dump


def init():
    update_data.convert_data()


def dump_all():
    dump.dump_all(config.dump_data_path)
