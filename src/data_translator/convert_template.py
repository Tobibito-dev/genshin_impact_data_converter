import json

from . import conversion_methods


def convert_data(genshin_data_path, template, languages):
    source_data = get_source_data(genshin_data_path, template)
    template_data = template['data']
    converted_data = {}
    unknown = 0

    for item in source_data['main']:
        converted_object = {}
        unknown

        for template_key in template_data:
            source_file = source_data[template_data[template_key]['path']]
            source_key = template_data[template_key]['key']
            conversion_method = template_data[template_key]['conversionMethod']
            if conversion_method == 'direct':
                attribute = conversion_methods.direct.convert(item, source_key)
            elif conversion_method == 'textMap':
                attribute = conversion_methods.text_map.convert(item, source_key, languages)
            else:
                print("not a valid conversion Method")
                attribute = None
            converted_object[template_key] = attribute

        name = converted_object['name']['en']
        key = name.lower().replace(' ', '_').replace('-', '_').replace("'", '')
        if key == 'none':
            key = 'unknown' + str(unknown)
            unknown = unknown + 1
        converted_data[key] = converted_object
    converted_data['unknownCount'] = unknown
    return converted_data


def get_source_data(genshin_data_path, template):
    source_data = {}
    for template_path in template['paths']:
        template_path_string = template['paths'][template_path]
        full_path_string = genshin_data_path + template_path_string
        source_data[template_path] = json.loads(open(full_path_string, encoding='utf8').read())
    return source_data
