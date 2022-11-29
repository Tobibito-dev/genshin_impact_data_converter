from ..util import text_map_util


def convert(languages, current_source_item, source_key):
    values = {}

    text_values = []
    source_values = []
    source_value = current_source_item[source_key]

    if type(source_value) != list:
        source_values.append(source_value)
    else:
        source_values = source_value

    for text_key in source_values:
        text_map_hash = str(text_key)
        text_value = text_map_util.get_values_from_languages(languages, text_map_hash)
        if text_value['en'] != 'None':
            text_values.append(text_value)

    for language_key in languages:
        values[language_key] = ''
        for index, value in enumerate(text_values):
            values[language_key] = values[language_key] + value[language_key]
            if index != (len(text_values)-1):
                values[language_key] = values[language_key] + ' '
    return values
