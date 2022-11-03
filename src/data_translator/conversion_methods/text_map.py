from .. import util


def convert(current_source_data, source_key, languages):
    values = {}

    for language_key in languages:
        text_map_hash = str(current_source_data[source_key])
        values = util.text_map_util.get_values_from_languages(languages, text_map_hash)
    return values
