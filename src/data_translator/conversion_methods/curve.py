import numbers


def convert(current_source_item, source_file, source_key):
    values = {}

    for level in source_file:
        stats = []

        for stat in current_source_item[source_key]:
            temp_stat = {}
            for value in stat:
                curve_type = None
                if type(stat[value]) == str and stat[value].startswith('GROW_CURVE'):
                    curve_type = stat[value]
                elif type(stat[value]) == float:
                    init_value = stat[value]
                    print(init_value)

                    temp_stat['value'] = init_value

            stats.append(temp_stat)

        values[level['level']] = stats
    return values
