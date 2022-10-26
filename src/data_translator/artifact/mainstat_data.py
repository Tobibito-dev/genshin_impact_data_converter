import json


class ArtifactMainStatData:
    def __init__(self,
                 rank: int,
                 level: int,
                 exp: int,
                 add_props: list,
                 ):
        self.rank = rank
        self.level = level
        self.exp = exp
        self.add_props = add_props


def return_mainstat_data(origin_file_path):
    temp_json_string = open(origin_file_path).read()
    temp_artifact_mainstats = json.loads(temp_json_string)
    artifact_mainstat_data = []
    for item in temp_artifact_mainstats:
        artifact_mainstat = ArtifactMainStatData(
            check_artifact_mainstat_key(item, 'rank'),
            check_artifact_mainstat_key(item, 'level'),
            check_artifact_mainstat_key(item, 'exp'),
            check_artifact_mainstat_key(item, 'addProps')
        )
        artifact_mainstat_data.append(artifact_mainstat)
    return artifact_mainstat_data


def check_artifact_mainstat_key(item, key: str):
    if key in item:
        value = item[key]
    else:
        value = None
    return value
