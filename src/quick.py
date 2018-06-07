import json
import networkx as nx
import matplotlib.pyplot as plt
from spacy.lang.en import STOP_WORDS
#from dependencies import extract_text
import spacy

G = nx.Graph()

G.add_edge("word1","word2")

edges = {("word1","word2") : "test"}


nx.draw(G, with_labels = True)
nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels = edges)

plt.show()