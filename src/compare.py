import spacy
import pandas as pd



def compare(doc1, doc2) :
    return doc1.similarity(doc2)


# def compare_abstracts(doc1, doc2) :
#     abstract1 = nlp(doc.text[doc1.text.index("Abstract")+8:doc1.text.index("1 Introduction")])
#     abstract2 = nlp(doc.text[doc2.text.index("Abstract")+8:doc2.text.index("1 Introduction")])
