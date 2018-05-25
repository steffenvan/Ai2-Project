from preprocess import preprocess, remove_empty_lines, one_sentence_per_line
from create_df import create_df
from compare import compare
import pandas as pd
import os
import spacy
import numpy as np

use_df = 0        # not using the comparision dataframe for now, just converting xml to txt


xml_path = "../data/xml/"
txt_path = "../data/txt/"
new_path = "../data/new_xml/"

def process_new_xml() :
    new_files = os.listdir(new_path)
    num_new_files = len([elt for elt in new_files if elt.endswith('.xml')])

    for new_filename in new_files:
        if (new_filename.endswith(".xml") and (new_filename not in os.listdir(xml_path))) :  # check if a new file isn't already in the data base
            preprocess(new_path + new_filename, txt_path + new_filename[:-4] + ".txt" )
            remove_empty_lines(txt_path + new_filename[:-4] + ".txt")
            one_sentence_per_line(txt_path + new_filename[:-4] + ".txt")
            os.rename(new_path + new_filename, xml_path + new_filename)   # moves the initial .xml file from the new_xml to the xml folder




def process_new_xml_with_df(old_df) :    # preprocesses all the .xml files in the new_xml folder

    M = old_df.as_matrix()   # Matrix from the old dataFrame
    n = M.shape[1]

    num_new_files = len([elt for elt in os.listdir(new_path) if elt.endswith('.xml')])     # number of newly added .xml files

    N = np.ones((n+num_new_files,n+num_new_files))      # Matrix for the new dataFrame
    N[0:n,0:n] = M

    new_files = os.listdir(new_path)
    files = list(old_df.columns)

    if (num_new_files!=0) :

        i = 0            # currently comparing the i^th in the new_files list

        for new_filename in new_files:



            if (new_filename.endswith(".xml") and (new_filename not in os.listdir(xml_path))) :  # check if a new file isn't already in the data base
                preprocess(new_path + new_filename, txt_path + new_filename[:-4] + ".txt" )
                remove_empty_lines(txt_path + new_filename[:-4] + ".txt")
                os.rename(new_path + new_filename, xml_path + new_filename)   # moves the initial .xml file from the new_xml to the xml folder




                new_doc = nlp(open(txt_path + new_filename[:-4] + ".txt").read())


                j = 0

                for old_filename in files :                   # comparision between the new file and all the old ones
                    old_doc = nlp(open(txt_path + old_filename).read())
                    val = compare(new_doc, old_doc)
                    #val = old_doc.similarity(new_doc)
                    N[n+i,j] = val
                    N[j,n+i] = val
                    j+=1
                    print(str(i+j) + " comparisions complete")

                files.append(new_filename[:-4] + ".txt")
                i += 1



        for i in range(num_new_files) :              # set the new diagonal terms to 1
            N[n+i, n+i] = 1

        if (num_new_files) :
            print(str(num_new_files) + " new file" + (num_new_files>1)*"s" + " pre-processed.")

        else :
            print("No new file to process.")

        return(pd.DataFrame(N, columns = files, index = files))

    else :

        print("No new file to process.")

        return(sim)

if (use_df) :
    nlp = spacy.load('en')


    if (os.path.exists("../data/similarities.pkl")) :

        sim = pd.read_pickle("../data/similarities.pkl")

    else :

        create_df()

        sim = pd.read_pickle("../data/similarities.pkl")

    new_df = process_new_xml_with_df(sim)

    new_df.to_pickle("../data/similarities.pkl")


else :
    process_new_xml()
