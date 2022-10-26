import os

def crawl_object(obj, keys, validate, cb):
    # TODO: crawl object
    pass


def layered_assignment(obj, keys, value):
    # TODO: layered assignment
    pass


def dump_file(file_path, new_file_path):
    obj = open(file_path)
    os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
    f = open(new_file_path, 'a')
    f.write(obj.read())
