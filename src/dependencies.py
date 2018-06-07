import json
import networkx as nx
import matplotlib.pyplot as plt
from spacy.lang.en import STOP_WORDS
import string
        
def extract_text(frame, vocab = [], stopwords = [], punct = []) :      # given a frame, extract all the text from frameElements / spans
    tokens = []
    for fe in frame["annotationSets"][0]["frameElements"] :
        
        tokens += fe["spans"][0]["text"].split()
    
    tokens += frame["target"]["spans"][0]["text"]
    
    
        
    L = list(map(str.lower,list(set(tokens))))
    
    if len(stopwords+punct) :
        L = [elt for elt in L if elt not in stopwords+punct+list(" ")]    # remove stopwords / punctuation if specified 
        
    if len(vocab) :
        L = [elt for elt in L if elt in vocab]                            # only keep words from a specified vocabulary if specified
        
    return L

def abstract(file) :                    # file = path / filename

    full_output = json.load(open(file))
    i = 0
    while ("Abstract" not in full_output[i]["tokens"]) :
        i += 1
    beg = i
    while ("Introduction" not in full_output[i]["tokens"]) :
        i += 1
    end = i
    return full_output[beg:end]
    
    


json_path = "../data/json/"

filename = "E09-1018-parscit.130908-11.49.59.json"

output = json.load(open(json_path + filename))


abs = abstract(json_path+filename)

vocab = []

for sentence in abs :
    vocab += (sentence["tokens"])

vocab = list(map(str.lower,list(set(vocab))))


stopwords = list(STOP_WORDS)+list("azertyuiopqsdfghjklmwxcvbn")

punct = list(string.punctuation)

G = nx.Graph()

edges = {}

for sentence in output[:50] :                   # this loop builds the dependency graph
    for frame in sentence["frames"] :
        L = extract_text(frame, vocab, stopwords, punct = punct)      # an edge is built between every word from the vocab ...
        # M = extract_text(frame, stopwords = stopwords, punct = punct)     # and every word in the whole text, if they appear at least once in the same frame
        for word1 in L :
            for word2 in L :
                if word1 != word2 :
                    G.add_edge(word1,word2)
                    edges[(str(word1), str(word2))] = str(frame["target"]["name"])

nx.draw(G, pos=nx.spring_layout(G), with_labels = True)

plt.show()

    
    