import json
import networkx as nx
import matplotlib.pyplot as plt
from spacy.lang.en import STOP_WORDS
#from dependencies import extract_text
import spacy
import os
from xml.dom import minidom

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

# xml_path = "../data/xml/"
# 
# filename = "E09-1018-parscit.130908-11.49.59.xml"
# 
# file = xml_path + filename
# 
# tree = ET.ElementTree(file = file)
# 
# for elt in tree.iter() :
#     print(elt.tag)

nlp = spacy.load('en')

print(str('apple' in nlp.vocab) )