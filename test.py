import src as gidm

gidm.init()

object = gidm.get_object('characters', 'albedo')
for key in object.data:
    print(object.get_value(key))

# print(object.get_stats(90))
