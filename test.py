import src as gidm

gidm.init()

character = gidm.get_object('weapons', 'primordial_jade_winged_spear')
for key in character.data:
    print(getattr(character, key))
