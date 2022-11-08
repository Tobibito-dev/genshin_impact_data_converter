import json

from . import conversion_methods


def convert_template_data(genshin_data_path, languages, template):
    source_data = get_source_data(genshin_data_path, template)
    item_type = template['type']
    template_data = template['data']
    converted_data = {}
    unknown = 0

    for src_item in source_data['main']:
        converted_object = {}

        for template_key in template_data:
            template_value = template_data[template_key]

            attribute = convert_one_template_value(
                genshin_data_path, languages, source_data, src_item, item_type, template_value)
            converted_object[template_key] = attribute

        name = converted_object['name']['en']
        key = name_to_key(name)
        if key == '':
            key = 'unknown' + str(unknown)
            unknown = unknown + 1

        converted_data[key] = converted_object

    converted_data['unknownCount'] = unknown
    return converted_data


def convert_one_template_value(genshin_data_path, languages, source_data, src_item, item_type, template_value):
    source_path = template_value['path']
    source_file = source_data[source_path]
    source_key = template_value['key']
    conversion_method = template_value['conversionMethod']

    if conversion_method == 'curve':
        attribute = conversion_methods.curve.convert(src_item, source_file, source_key)
    elif conversion_method == 'direct':
        attribute = conversion_methods.direct.convert(src_item, source_key)
    elif conversion_method == 'readable':
        attribute = conversion_methods.readable.convert(genshin_data_path, languages, item_type, src_item, source_key)
    elif conversion_method == 'stat':
        attribute = conversion_methods.stat.convert(src_item, source_file, source_key)
    elif conversion_method == 'textMap':
        attribute = conversion_methods.text_map.convert(languages, src_item, source_key)
    else:
        print("not a valid conversion Method")
        attribute = None
    return attribute


def get_source_data(genshin_data_path, template):
    source_data = {}
    for template_path in template['paths']:
        template_path_string = template['paths'][template_path]
        full_path_string = genshin_data_path + template_path_string
        with open(full_path_string, encoding='utf8') as path_file:
            source_data[template_path] = json.loads(path_file.read())
    return source_data


def name_to_key(name: str):
    key = name.lower()
    key = key.replace(' ', '_').replace('-', '_')
    chars = ["'",  '"', '.', '?', '!', '#']
    for char in chars:
        key = key.replace(char, '')
    return key
