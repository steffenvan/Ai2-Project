import json
from extraction import *
from path import root

toy_path = root + 'data/toy_examples/'

neg_file = "E09-1008-parscit.neg"
frames_file = "E09-1008-parscit.130908-11.49.59.json"

neg = json.load(open(toy_path + neg_file))
frames = json.load(open(toy_path + frames_file))

for i in range(len(neg_file)) :
    print(neg[i])
    print(frames[i])
    print("*****************")