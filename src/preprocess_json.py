"""
This script aims at fixing an issue on the raw output of semafor, which is not directly
readable by the json python module.
It goes through the new_json folder (outputs from semafor) and performs small
modifications on each one. The modified files are saved into the json folderself.
"""

import os

raw_json_path = "../data/new_json/"
processed_json_path = "../data/json/"

for filename in os.listdir(raw_json_path) :
    if filename.endswith(".json") :
        file = open(raw_json_path + filename, 'r')
        raw = file.read()

        string = "["

        for c in raw :
            if c == '\n' :
                string += ","
            else :
                string += c

        string = string[:-1]

        string += "]"

        file.close()

        os.remove(raw_json_path + filename)

        processed = open(processed_json_path + filename, 'w+')

        processed.write(string)

        processed.close()
