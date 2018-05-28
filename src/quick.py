"""
NOTE : this is a toy script just for running quick experiments
"""
import spacy
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

json_path = "../data/json/"

frames = {}

print("d" in frames)

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

# sns.distplot((df.sort_values(['quantity'], axis = 1, ascending = False).head(15)))

print(df.sort_values(['quantity'], axis = 1, ascending = False).head(15))
#
sns.barplot(frames)
# #
plt.xlabel(df.columns)
plt.show()
# #
# print(df.head(100))
