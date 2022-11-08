import src as gidm

gidm.init()

character = gidm.get_object('characters', 'albedo')
for key in character.data:
    print(getattr(character, key))
