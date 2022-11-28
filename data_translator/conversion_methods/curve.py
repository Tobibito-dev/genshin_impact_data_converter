def convert(current_source_item, source_file, source_key):
    values = {}
    stat_types = []
    curve_types = []

    for index, stat in enumerate(current_source_item[source_key]):
        for value in stat:
            if type(stat[value]) == str and stat[value].startswith('GROW_CURVE'):
                curve_type = stat[value]
                curve_types.append(curve_type)
            elif type(stat[value]) == str and stat[value].startswith('FIGHT_PROP'):
                stat_type = stat[value]
                stat_types.append(stat_type)

        if len(curve_types) <= index:
            curve_types.append(None)
        if len(stat_types) <= index:
            stat_types.append(None)

    for level in source_file:
        stats = []
        for index, curve_type in enumerate(curve_types):
            stat_curve = {}

            for curve in level['curveInfos']:
                if curve['type'] == curve_type:
                    stat_curve['type'] = stat_types[index]
                    stat_curve['value'] = curve['value']
                    stat_curve['arith'] = curve['arith']
                    stats.append(stat_curve)

        values[level['level']] = stats
    return values
