def convert(current_source_item, source_data, source_path, source_key):
    values = []
    keys = None

    depot_id = current_source_item['skillDepotId']
    depot = source_data['depot']
    skill_source = source_data[source_path]

    for skill in depot:
        if skill['id'] == depot_id:
            keys = skill[source_key]
            break

    for key in keys:
        for skill_data in skill_source:
            pass

        values.append(key)

    return values
