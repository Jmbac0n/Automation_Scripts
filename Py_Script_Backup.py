import os, shutil

path = 'C:/Users/Jake/AppData/Local/Programs/Python/Python38/MyScripts'

print("Before moving file:")
print(os.listdir(path))

Source = 'C:/Users/Jake/AppData/Local/Programs/Python/Python38/MyScripts/Source'

Destination = 'C:/Users/Jake/AppData/Local/Programs/Python/Python38/MyScripts/Destination'

dest = shutil.copy(Source, Destination)

print("After moving file:")
print(os.listdir(path))

print("Destination path:", dest)

#TODO

#Sort out permissions problem for copying the test source to test dest