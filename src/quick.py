import spacy
import os
import json
from random import shuffle

nlp = spacy.load('en')

json_path = "../data/json/"

def display_frame_instances_with_pos(frame_name, nmax = 5) :    # prints all the instances of a given frame among the toy dataset

    os.system("clear")

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

                            if frame["target"]["name"] == frame_name :

                                curr_sentence = " ".join(sentence["tokens"])
                                pos = [str(token.pos_) for token in nlp(str(curr_sentence))]
                                string = ""
                                for k in range(len(list(sentence["tokens"]))) :
                                    string += (sentence["tokens"][k])
                                    string += (' [' + pos[k] + '] ')

                                print(string)
                                print('\n')
                                i += 1


display_frame_instances_with_pos("Desirability", 5)
