import json
import networkx as nx
import matplotlib.pyplot as plt
from spacy.lang.en import STOP_WORDS
import string
from path import root
from extraction import *      


json_path =  root + "data/json/"

filename = "E09-1018-parscit.130908-11.49.59.json"

output = json.load(open(json_path + filename))


abs = abstract_json(json_path+filename)
ccl = conclusion_json(json_path+filename)

vocab = []
# 
for sentence in abs :
    vocab += (sentence["tokens"])

print(vocab)

vocab = list(map(str.lower,list(set(vocab))))   # removes duplicates


stopwords = list(STOP_WORDS)+list("azertyuiopqsdfghjklmwxcvbn")

punct = list(string.punctuation)

G = nx.Graph()

edges = {}

for sentence in abs :                   # this loop builds the dependency graph
    for frame in sentence["frames"] :
        L = extract_text(frame, vocab, stopwords = stopwords, punct = punct) 
        M = extract_text(frame, stopwords = stopwords, punct = punct)     
        for word1 in L :
            for word2 in M :
                if word1 != word2 :
                    G.add_edge(word1,word2)
                    edges[(str(word1), str(word2))] = str(frame["target"]["name"])

nx.draw(G, pos=nx.spring_layout(G), with_labels = True)

plt.show()


    