import os

for file in os.listdir() :
    if file.endswith(".txt") or file.endswith(".xml"):
        os.rename(file, file.replace(" ", "-"))
