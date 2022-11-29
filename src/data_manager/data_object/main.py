from . import get_stats


class DataObject:
    def __init__(self, object_data: dict):
        self.data = object_data
        if type(object_data) != int:
            for key in object_data:
                setattr(self, key, object_data[key])

    def get_value(self, key: str):
        value = getattr(self, key)
        return value

    def get_stats(self, level: int, promoted=False):
        stats = get_stats.from_level(self, level, promoted)
        return stats
