import src as gidm
from src.data_manager.storage import data

gidm.init()

gidm.dump_all()

print(data['characters']['Bennett']['talents'])
