import spacy
import pandas as pd



def compare(doc1, doc2) :
    return doc1.similarity(doc2) 
