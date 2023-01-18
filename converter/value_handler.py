from . import text_map_util


def get_key_value_pair(source_key, source, files, var_value=None):
    if source_key.startswith('$'):
        if '*' in source_key:
            key_variations = get_all_variable_variations(get_path(source_key), files)
            key = []
            value = []
            for variation in key_variations:
                path_variation = replace_path_variable(get_path(source_key), variation)
                key.append(get_data_from_path(path_variation, files))
                value.append(get_value(source, files, variation))

        else:
            key = str(get_value(source_key, files))
            value = get_value(source, files, var_value)
    else:
        key = source_key
        value = get_value(source, files, var_value)

    return key, value

def get_value(source, files, var_value=None):
    if type(source) == str:
        if source.startswith('$'):
            value = get_data_from_path(get_path(source), files, var_value)
        else:
            value = source
    elif type(source) == list:
        value = []
        for sub_source in source:
            value.append(get_value(sub_source, files, var_value))
    elif type(source) == dict:
        value = {}
        for source_key in source:
            new_key, new_value = get_key_value_pair(source_key, source[source_key], files, var_value)
            if type(new_key) == list:
                for index, key in enumerate(new_key):
                    value[key] = new_value[index]
            else:
                value[new_key] = new_value
    else:
        value = 'Template Error: please review data paths in template.'

    return value

def get_data_from_path(path, files, var_value=None):
    last_value = 'No data in this location'
    data = files['entry']
    for step in path:
        if step == '*' and not var_value is None:
            step = var_value
        if type(step) == str:
            if step in files:
                data = files[step]
            elif step == 'text_map':
                data = text_map_util.get_values_from_languages(str(last_value))
            elif step in data:
                data = data[step]
                if not type(data) == list and not type(data) == dict:
                    last_value = data
            elif '.' in step and '=' in step:
                filter_key = step.split('=')[0].split('.')
                filter_value = step.replace('.', '').split('=')[1]
                data = filter_for_value(data, filter_key, filter_value)
            elif '.' in step and '=' not in step:
                filter_key = step.split('.')
                data = filter_for_value(data, filter_key, last_value)
            else:
                data = 'Step Type Error: unexpected data type in template'
                break
        elif type(step) == int:
            if type(data) == list:
                data = data[step]
            elif step >= 1:
                data = "Doesn't exist on this Item"
                break
        else:
            data = 'Step Type Error: unexpected data type in template'
            break

    return data


def filter_for_value(source_data, filter_key: list, filter_value):
    value = []

    for sub_source in source_data:
        if type(sub_source) == str:
            sub_source = source_data[sub_source]
        temp_source = sub_source
        for step in filter_key:
            if step in temp_source and not step == '':
                temp_source = temp_source[step]
        if temp_source == filter_value:
            value.append(sub_source)

    if len(value) == 1:
        value = value[0]

    return value

def get_all_variable_variations(path, files):
    base_path = []
    for step in path:
        if step == '*':
            break
        else:
            base_path.append(step)

    ast_source = get_data_from_path(base_path, files)
    variable_variations = []
    for index, sub_source in enumerate(ast_source):
        if type(ast_source) == dict:
            variable_variations.append(sub_source)
        elif type(ast_source) == list:
            variable_variations.append(index)
    return variable_variations

def replace_path_variable(path, value):
    new_path = []
    for step in path:
        if step == '*':
            new_path.append(value)
        else:
            new_path.append(step)
    return new_path

def get_path(source):
    path = source.replace('$', ''). split('/')

    for index, step in enumerate(path):
        if step.startswith('#'):
            path[index] = int(step.replace('#', ''))
    return path
