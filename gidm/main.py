from .translate import translate_data
from .text_map_util import init_languages

def run():
    # check if data exists
    init_languages()
    translate_data()
    # print status
    pass
