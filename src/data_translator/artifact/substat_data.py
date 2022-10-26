import json


class ArtifactSubStatData:
    def __init__(self,
                 id: int,
                 depot_id: int,
                 group_id: int,
                 prop_type: str,
                 prop_value: int):
        self.id = id
        self.depot_id = depot_id
        self.group_id = group_id
        self.prop_type = prop_type
        self.prop_value = prop_value


def return_substat_data(origin_file_path):
    temp_json_string = open(origin_file_path).read()
    temp_artifact_substats = json.loads(temp_json_string)
    artifact_substat_data = []
    for item in temp_artifact_substats:
        artifact_substat = ArtifactSubStatData(
            check_artifact_substat_key(item, 'id'),
            check_artifact_substat_key(item, 'depotId'),
            check_artifact_substat_key(item, 'groupId'),
            check_artifact_substat_key(item, 'propType'),
            check_artifact_substat_key(item, 'propValue')
        )
        artifact_substat_data.append(artifact_substat)
    return artifact_substat_data


def check_artifact_substat_key(item, key: str):
    if key in item:
        value = item[key]
    else:
        value = None
    return value
