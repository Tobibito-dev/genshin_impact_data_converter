from . import text_map_util


def get_value(source, files):
    if type(source) == str:
        path = get_value_path(source)
        if type(path) == str:
            return path
        else:
            return get_value_from_path(path, files)
    else:
        if type(source) == list:
            return get_list_value_paths(source, files)
        elif type(source) == dict:
            return get_dict_value_paths(source, files)


def get_value_from_path(path, files):
    current_file = 'entry'
    current_data = files[current_file]
    value = None
    for step in path:
        if step in files:
            current_file = step
            current_data = files[current_file]
        elif step == 'text_map':
            value = text_map_util.get_values_from_languages(str(value))
            break
        elif step.startswith('.'):
            filter_key = step.replace('.', '')
            current_data = filter_for_object(filter_key, value, current_data)
        elif type(current_data) == dict:
            if step in current_data:
                value = current_data[step]

    return value


def filter_for_object(filter_key, filter_value, filter_data):
    for item in filter_data:
        if filter_key in item:
            if filter_value == item[filter_key]:
                return item


def get_list_value_paths(source: list, files):
    values = []
    for sub_source in source:
        values.append(get_value(sub_source, files))
    return values


def get_dict_value_paths(source: dict, files):
    values = {}
    for sub_source in source:
        values[sub_source] = get_value(source[sub_source], files)
    return values


def get_value_path(source: str):
    if source.startswith('$'):
        return source.replace('$', '').split('/')
    else:
        return source
