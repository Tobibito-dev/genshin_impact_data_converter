from . import text_map_util


def get_key_value_pair(source_key, source, files):
    if source_key.startswith('$'):
        if '*' in source_key:
            key = '*'
            value = '*'
        else:
            key = str(get_value(source_key, files))
            value = get_value(source, files)
    else:
        key = source_key
        value = get_value(source, files)

    return key, value

def get_value(source, files):
    if type(source) == str:
        if source.startswith('$'):
            value = get_data_from_path(get_path(source), files)
        else:
            value = source
    elif type(source) == list:
        value = []
        for sub_source in source:
            value.append(get_value(sub_source, files))
    elif type(source) == dict:
        value = {}
        for source_key in source:
            new_key, new_value = get_key_value_pair(source_key, source[source_key], files)
            value[new_key] = new_value
    else:
        value = 'Template Error: please review data paths in template.'

    return value

def get_data_from_path(path, files):
    last_value = 'No data in this location'
    data = files['entry']
    for step in path:
        if type(step) == str:
            if step in files:
                data = files[step]
            elif step == 'text_map':
                data = text_map_util.get_values_from_languages(str(last_value))
            elif step in data:
                data = data[step]
                last_value = data
            elif '.' in step and '=' in step:
                filter_key = step.replace('.', '').split('=')[0]
                filter_value = step.replace('.', '').split('=')[1]
                data = filter_for_value(data, filter_key, filter_value)
            elif '.' in step and '=' not in step:
                filter_key = step.replace('.', '')
                data = filter_for_value(data, filter_key, last_value)
        elif type(step) == int:
            data = data[step]
        else:
            data = 'Step Type Error: unexpected data type in template'

    return data


def filter_for_value(source_data, filter_key: str, filter_value):
    value = []
    for sub_source in source_data:
        if type(sub_source) == str:
            sub_source = source_data[sub_source]
        if filter_key in sub_source:
            if sub_source[filter_key] == filter_value:
                value.append(sub_source)

    if len(value) == 1:
        value = value[0]

    return value

def get_path(source_str: str):
    path = source_str.replace('$', ''). split('/')

    for index, step in enumerate(path):
        if step.startswith('#'):
            path[index] = int(step.replace('#', ''))


    return path
