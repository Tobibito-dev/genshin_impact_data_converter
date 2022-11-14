import src as gidm

gidm.init()

artifact = gidm.get_object('artifacts', 'LavawalkersEpiphany')
char = gidm.get_object('characters', 'Bennett')
weapon = gidm.get_object('weapons', 'MistsplitterReforged')
for key in artifact.data:
    print(artifact.get_value(key))
    pass

print('')
# print(char.get_stats(90))
# print(weapon.get_stats(90))

gidm.dump_all()

