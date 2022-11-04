from ..util import text_map_util


def convert(languages, current_source_item, source_key):
    values = {}
    text_map_hash = str(current_source_item[source_key])
    values = text_map_util.get_values_from_languages(languages, text_map_hash)
    return values
