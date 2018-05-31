import spacy
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

json_path = "../data/json/"

frames = {}

for filename in os.listdir(json_path) :
    if filename.endswith(".json") :
        output = json.load(open(json_path + filename))
        for sentence in output :
            for frame in sentence["frames"] :
                frame_name = frame["target"]["name"]
                if (frame_name in frames) :
                    frames[frame_name] += 1
                else :
                    frames[frame_name] = 1



df = pd.DataFrame(frames, index = ['quantity'])

df = df.sort_values(['quantity'], axis = 1, ascending = False)

df = df.transpose()

df.to_pickle("../data/frames.pkl")
