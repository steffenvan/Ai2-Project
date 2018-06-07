import spacy
import json
import os
from preprocess import remove_empty_lines
from article import *


xml_path = "../data/xml/"

target_path = "../data/titles/"

L = []
for filename in os.listdir(xml_path) :
    if filename.endswith(".xml") :
        L.append(Article(filename[:-4]))

print(len(L))
