import src as gidm

gidm.init()

object = gidm.get_object('weapons', 'primordial_jade_winged_spear')
for key in object.data:
    print(object.get_value(key))

print(object.get_stats(90))
