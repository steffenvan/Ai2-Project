"""
NOTE : this is a toy script just for running quick experiments
"""
import spacy
import os

nlp = spacy.load('en')

doc = nlp("this is a test for detecting end-of-line hyphens.")

for token in doc :
    print(token.text + " " + str(token.is_punct))


assert "blubd" in nlp.vocab
