import os


# check if GenshinData exists
def check_data():
    if os.path.isdir('./GenshinData/.git/'):
        print("updating genshin genshin_data_manager")
        update_data()
    else:
        print("GenshinData missing")
        get_data()


# clone dimbreath GenshinData repo
def get_data():
    os.system('git clone --progress https://github.com/Dimbreath/GenshinData.git ../GenshinData/ --depth 1')


# pull dimbreath GenshinData repo
def update_data():
    os.system('cd ./GenshinData/ && git fetch --progress --depth 1 && git reset --hard origin/master')

check_data()