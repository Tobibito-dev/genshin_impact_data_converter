def convert(current_source_item, source_file, source_key):
    promote_id = current_source_item[source_key]

    promote_list = []

    for promote_level in source_file:
        if promote_level[source_key] == promote_id:
            if 'promoteLevel' not in promote_level:
                promote_level['promoteLevel'] = 0
            promote_list.append(promote_level)

    return promote_list
