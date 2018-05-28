import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
import json

json_path = "../data/json/"

def display_frame_instances(frame_name, nmax = 5) :    # prints all the instances of a given frame among the toy dataset

    i = 1

    for filename in os.listdir(json_path) :

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

                            if frame["target"]["name"] == frame_name :

                                print(" ".join(sentence["tokens"]))

                                i += 1



display_frame_instances("Desirability", 15)
