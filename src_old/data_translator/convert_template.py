import json

from . import conversion_methods


def convert_template_data(genshin_data_path, languages, template, pre_release: bool):
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

        if item_released(source_data, converted_object['id']) or pre_release:
            converted_data[key] = converted_object

    if pre_release:
        converted_data['unknownCount'] = unknown
    return converted_data


def convert_one_template_value(genshin_data_path, languages, source_data, src_item, item_type, template_value):
    source_path = template_value['path']
    source_file = source_data[source_path]
    source_key = template_value['key']
    source_key_list = template_value.get('key_list', None)
    conversion_method = template_value['conversionMethod']

    if conversion_method == 'baseStat':
        attribute = conversion_methods.base_stat.convert(src_item, source_key, source_key_list)
    elif conversion_method == 'curve':
        attribute = conversion_methods.curve.convert(src_item, source_file, source_key)
    elif conversion_method == 'direct':
        attribute = conversion_methods.direct.convert(src_item, source_key)
    elif conversion_method == 'promote':
        attribute = conversion_methods.promote.convert(src_item, source_file, source_key)
    elif conversion_method == 'readable':
        attribute = conversion_methods.readable.convert(genshin_data_path, languages, item_type, src_item, source_key)
    elif conversion_method == 'talent':
        attribute = conversion_methods.talent.convert(src_item, source_data, source_path, source_key)
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


def item_released(source_data, item_id):
    if 'codex' in source_data:
        codex = source_data['codex']
        released = False
        for item in codex:
            if 'isDisuse' not in item:
                for value in item:
                    if item[value] == item_id:
                        released = True
                        break
            if released:
                break
    else:
        released = True
    return released


def name_to_key(name: str):
    key = name.replace("'", '').title()
    chars = ['"', '.', '?', '!', '#', ' ', '-', ':']
    for char in chars:
        key = key.replace(char, '')
    return key
