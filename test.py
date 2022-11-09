import src as gidm

gidm.init()

object = gidm.get_object('weapons', 'deicide')
for key in object.data:
    print(object.get_value(key))

print('')
print(object.get_stats(90))

