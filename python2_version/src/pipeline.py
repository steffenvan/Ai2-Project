from article import *
import os
from preprocess_functions import *


"""
to add new xml files to the database, simply drag them to data/xml/ and then run this script
"""
ai2_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
print('ai2 :' + ai2_path)
root = os.path.abspath(os.path.join(ai2_path, os.pardir))

xml_path = ai2_path + "/data/xml/"
txt_path = ai2_path + "/data/txt/"
path = ai2_path + "/data/"

if (os.path.isfile(path + "corpus_words.txt") == 0) :    # creation of corpus_words.txt if needed
    newfile = open(path + "corpus_words.txt","w+")
    newfile.close()
    

L = []

for filename in os.listdir(xml_path) :
    if filename.endswith(".xml") :
        try :
            L.append(Article(filename[:-4]))
        except :
            os.rename(xml_path + filename, path + "rejected/" + filename)

print("Currenlty " + str(len(L)) + " files fully pre-processed." )