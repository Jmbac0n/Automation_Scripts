import os, shutil

Source = 'C:/Users/Jake/AppData/Local/Programs/Python/Python38/MyScripts'
Destination = 'D:/MyScripts'


def remove_old_backup():
    shutil.rmtree(Destination)

def create_backup():
    path = 'C:/Users/Jake/AppData/Local/Programs/Python/Python38/MyScripts'

    print("Before moving file:")
    print(os.listdir(path))

    dest = shutil.copytree(Source, Destination)

    print("After moving file:")
    print(os.listdir(path))

    print("Destination path:", dest)

remove_old_backup()
create_backup()

#TODO

#Sort out permissions problem for copying the test source to test dest