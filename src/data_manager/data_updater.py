import os


# check if genshin_data exists
def check_data():
    if os.path.isdir('./genshin_data/.git/'):
        print("updating genshin genshin_data_manager")
        update_data()
    else:
        print("genshin_data missing")
        get_data()


# clone dimbreath genshin_data repo
def get_data():
    os.system('git clone --progress https://github.com/Dimbreath/GenshinData.git ../genshin_data/ --depth 1')


# pull dimbreath genshin_data repo
def update_data():
    os.system('cd ./genshin_data/ && git fetch --progress --depth 1 && git reset --hard origin/master')

check_data()