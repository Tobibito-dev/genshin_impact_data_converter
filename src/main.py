import update_data
import config
import pprint

from data_manager import data
from data_manager import dump

update_data.convert_data()

dump.dump_all(config.dump_data_path)
