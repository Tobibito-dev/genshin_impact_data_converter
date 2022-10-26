import os


# check if GenshinData exists
def check_data(genshin_data_path):
    if os.path.isdir(genshin_data_path + '.git/'):
        print("pulling genshin_data")
        update_data(genshin_data_path)
    else:
        print("GenshinData missing")
        get_data(genshin_data_path)


# pull dimbreath GenshinData repo
def update_data(genshin_data_path):
    os.system('cd ' + genshin_data_path + ' && git fetch --progress --depth 1 && git reset --hard origin/master')


# clone dimbreath GenshinData repo
def get_data(genshin_data_path):
    os.system('git clone --progress https://github.com/Dimbreath/GenshinData.git ' + genshin_data_path + ' --depth 1')
