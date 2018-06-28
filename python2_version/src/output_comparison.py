import json
from extraction import *
from path import root

toy_path = root + 'data/toy_examples/'

neg_file = "E09-1005-parscit.json"
frames_file = "E09-1005-parscit.130908-11.49.59.json"
text_file = "E09-1005-parscit.130908-11.49.59.txt"

text = open(toy_path + text_file).read().split('\n')
neg = json.load(open(toy_path + neg_file))
frames = json.load(open(toy_path + frames_file))

for i in range(len(neg)) :
    print(text[i])
    print("\n")
    print("****")
    # print(neg[i])
    # print("\n")
    # print("****")
    # print([frames[i]["frames"][j]["target"]["name"] for j in range(len(frames[i]["frames"]))])
    for j in range(len(frames[i]["frames"])) :
        print("\n")
        frame = frames[i]["frames"][j]
        print("name : " + frame["target"]["name"])
        print("text : " + frame["target"]["spans"][0]["text"])
        print("Annotation Set :" + str(frame["annotationSets"][0]["frameElements"]))
    print("\n")
    print("**************************************************")
    print("\n")
    print("\n")
    print("\n")
    print("\n")