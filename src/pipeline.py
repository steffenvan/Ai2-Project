from article import *
import os
from preprocess_functions import *

xml_path = "../data/xml/"
txt_path = "../data/txt/"
path = "../data/"

if (os.path.isfile(path + "corpus_words.txt") == 0) :
    newfile = open(path + "corpus_words.txt","w+")
    newfile.close()
    

L = []

for filename in os.listdir(xml_path) :
    if filename.endswith(".xml") :
        L.append(Article(filename[:-4]))

print(len(L))