import os
import shutil

path = input("Enter directory: ")
files = os.listdir(path)

for file in files:
    extension = file.split(".")[-1]
    if os.path.exists(path+"/"+extension):
        shutil.move(path+"/"+file, path+"/"+extension+"/"+file)
    else:
        os.mkdir(path+"/"+extension)
        shutil.move(path+"/"+file, path+"/"+extension+"/"+file)
