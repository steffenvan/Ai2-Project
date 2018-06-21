import json
from extraction import *
from path import root

toy_path = root + 'data/toy_examples/'

neg_file = "E09-1005-parscit.json"
frames_file = "E09-1005-parscit.130908-11.49.59.json"

neg = json.load(open(toy_path + neg_file))
frames = json.load(open(toy_path + frames_file))

for i in range(len(neg)) :
    print(neg[i])
    print("****")
    print(frames[i])
    print("*****************")