"""
This file contains functions useful for preliminary data analysis, such as extraction of frames or sentences containing certain words
"""
import os
import json
from path import root
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from random import shuffle
from extraction import *

json_path =  root + "/data/json/"

def number_of_frames(json_file) :
    json_list = json.load(open(json_file))
    number_of_frames = 0
    
    for i in range(len(json_list)) :
        number_of_frames += len(json_list[i]["frames"])
    
    print("Total number of frames in the article : %d. Average number of frames per sentence : %d." %(number_of_frames,number_of_frames/len(json_list))) 
    
    return number_of_frames


def number_of_sentences(json_file) :
    json_list = json.load(open(json_file))
    print("Total number of sentences in the article : %d." %(len(json_list)))
    return number_of_sentences
    

# number_of_sentences(json_path + "E09-1005-parscit.130908-11.49.59.json")

def count_frames(in_abstract = 0) :
    
    counts = {}
    for filename in os.listdir(json_path) :
        
        if filename.endswith("json") :
            if in_abstract :
                doc = abstract_json(json_path + filename) 
            else :
                doc = json.load(open(json_path + filename)) 
                
            for sentence in doc :
                for frame in sentence["frames"] :
                    frame_name = frame["target"]["name"]
                    if frame_name in counts :
                        counts[frame_name] += 1
                    else : 
                        counts[frame_name] = 1            
    return counts
    
    
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

                                print(frame["target"]["name"] + ": " + " ".join(sentence["tokens"]))
                                print("\n")

                                i += 1

# relevant_frames = ["scale", "accomp"] # "accomp","accura","compar","relevant", "competition", "desirability", "scale"
# 
# for frame in relevant_frames :
#     display_frame_instances(frame, 5)            

# print(head(df))

# print(d)
# 
# print("total number of frames in the docs : %d" %(sum([val for val in d.values()])))
# 
# print("total number of frames in doc " + os.listdir(json_path)[2] + " : %d" %(number_of_frames(json_path + os.listdir(json_path)[2])))
