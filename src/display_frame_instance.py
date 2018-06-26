import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
import json
from random import shuffle
from extraction import *

json_path = "../data/json/"

def display_frame_instances(frame_name, nmax = 5, abstract = 0) :    # prints all the instances of a given frame among the toy dataset

    print("**************************************\n")

    files = os.listdir(json_path)

    shuffle(files)

    i = 1

    for filename in files :

        if i > nmax :

            break

        if filename.endswith(".json") :


            if i > nmax :

                break



            output = json.load(open(json_path + filename))

            for sentence in output :

                        if i > nmax :

                            break

                        for frame in sentence["frames"] :

                            if i > nmax :

                                break

                            if frame_name in frame["target"]["name"].lower() :

                                print(frame_name + ": " + " ".join(sentence["tokens"]))
                                print("\n")

                                i += 1


relevant_frames = ["scale", "accomp"] # "accomp","accura","compar","relevant", "competition", "desirability", "scale"

for frame in relevant_frames :
    display_frame_instances(frame, 5)
    

