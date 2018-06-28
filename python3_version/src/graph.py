import matplotlib.pyplot as plt
import string 
from path import root
from extraction import *
import json
from spacy.lang.en import STOP_WORDS
import networkx as nx

json_path = root + 'data/json/'

"""
this file is for building a dependency graph for one specific document
"""



def build_graph(filename, abs = 0, ccl = 0) :
    doc = []
    if abs == 1 :
        doc += abstract_json(filename)
    if ccl == 1 :
        doc += conclusion_json(filename)
    if abs + ccl == 0 :
        doc = json.load(open(filename))
        
    vocab = []
    # 
    for sentence in doc :
        vocab += (sentence["tokens"])
        
    vocab = list(map(str.lower,list(set(vocab)))) # removes duplicates
    stopwords = list(STOP_WORDS)+list("azertyuiopqsdfghjklmwxcvbn")
    punct = list(string.punctuation)

        
    G = nx.Graph()
    edges = {}
    
    for sentence in doc :
        for frame in sentence["frames"] :
            L = extract_text(frame, stopwords = stopwords, punct = punct)
            for word1 in L :
                for word2 in L :
                    if word1 != word2 :
                        G.add_edge(word1, word2)
                        edges[(str(word1), str(word2))] = str(frame["target"]["name"])
            
    # nx.draw(G, pos = nx.spring_layout(G), with_labels = True)
    # nx.draw_networkx_edge_labels(G, pos = nx.spring_layout(G))
    
    matrix = nx.to_numpy_matrix(G)

    # print matrix

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_aspect('equal')
    plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.gray)
    plt.show()
    # 
    # plt.show()    
    
     
        
build_graph(json_path + "E09-1018-parscit.130908-11.49.59.json", 0, 1)