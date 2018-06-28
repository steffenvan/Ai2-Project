from article import *
import os
from preprocess_functions import *
from path import root



"""
to add new xml files to the database, simply drag them to data/xml/ and then run this script
"""

xml_path = root + "data/xml/"
txt_path = root + "data/txt/"
path = root + "data/"

if (os.path.isfile(path + "corpus_words.txt") == 0) :    # creation of corpus_words.txt if needed
    newfile = open(path + "corpus_words.txt","w+")
    newfile.close()
    

L = []

for filename in os.listdir(xml_path) :
    if filename.endswith(".xml") :
        L.append(Article(filename[:-4]))

print("Currenlty " + str(len(L)) + " files fully pre-processed." )