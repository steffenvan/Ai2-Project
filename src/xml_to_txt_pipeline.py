from preprocess import preprocess, remove_empty_lines
import pandas as pd
import os

xml_path = "../data/xml/"
txt_path = "../data/txt/"
new_path = "../data/new_xml/"


# if (os.path.exists("../data/similarities.pkl")) :
#
#     sim = pd.read_pickle("../data/similarities.pkl")
#
# else :
#
#     sim = pd.DataFrame()
#
#
# M = sim.as_matrix()
# n = M.shape[1]


def process_new_xml() :    # preprocesses all the .xml files in the new_xml folder
    i = 0
    if (len(os.listdir(new_path))!=0) :
        files = os.listdir(new_path)
        for filename in files:
            if (filename[-3:] == "xml" and (filename not in os.listdir(xml_path))) :
                preprocess(new_path + filename, txt_path + filename[:-4] + ".txt" )
                remove_empty_lines(txt_path + filename[:-4] + ".txt")
                os.rename(new_path + filename, xml_path + filename)   # save the initial .xml files to the xml folder and suppress them from new_xml
                i += 1

        if (i) :
            print(str(i) + " files pre-processed.")

        else :
            print("No new file to process.")


    else :

        print("No new file to process.")

process_new_xml()
