import spacy
import json
import os
from preprocess import remove_empty_lines
from article import *


xml_path = "../data/xml/"

target_path = "../data/titles/"


# for filename in list(os.listdir(xml_path))[:2] :
#     if filename.endswith(".xml") :
#         source = open(xml_path + filename,'r').read()
#         target = open(target_path + "title" + '_' + filename,'w')
#         print(filename)
#         # print(source.find("<title"))
#         # print(source.find("</title"))
#         beg = source.find("<title")
#         beg2 = source[beg:].find(">")
#         target.write(source[beg + beg2 + 1 :source.find("</title")])
#         remove_empty_lines(target_path + "title" + '_' + filename)


a = Article("E09-1007-parscit.130908-11.49.59")
L = []
for filename in os.listdir(xml_path) :
    if filename.endswith(".xml") :
        L.append(Article(filename[:-4]))

print(len(L))
