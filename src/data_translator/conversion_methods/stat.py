
def convert(current_source_item, source_key, source_key_list):
    base_stats = []
    stat_types = []
    base_stat_values = []
    curve_types = []

    if source_key_list:
        for key in source_key_list:
            base_stat_value = current_source_item.get(key, 1)
            base_stat_values.append(base_stat_value)

    for index, stat in enumerate(current_source_item[source_key]):
        for value in stat:
            if type(stat[value]) == str and stat[value].startswith('GROW_CURVE'):
                curve_type = stat[value]
                curve_types.append(curve_type)
            elif type(stat[value]) == str and stat[value].startswith('FIGHT_PROP'):
                stat_type = stat[value]
                stat_types.append(stat_type)
            elif type(stat[value]) == float:
                base_value = stat[value]
                base_stat_values.append(base_value)

        if len(stat_types) <= index:
            stat_types.append(None)
        if len(base_stat_values) <= index:
            base_stat_values.append(1)
        if len(curve_types) <= index:
            curve_types.append(None)

    for index, stat_type in enumerate(stat_types):
        base_stat = {'type': stat_type,
                     'value': base_stat_values[index]}
        base_stats.append(base_stat)

    return base_stats
