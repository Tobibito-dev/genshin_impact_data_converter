from ..util import readable_util


def convert(genshin_data_path, languages, item_type, current_source_item, source_key):
    values = {}
    key_id = str(current_source_item[source_key])
    values = readable_util.get_readable_data(genshin_data_path, languages, key_id, item_type)
    return values
