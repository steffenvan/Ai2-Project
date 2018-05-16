import spacy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

noisy_pos_tags = ["IN"]

nlp = spacy.load("en")

doc = nlp(open("out.txt",'r').read())

words = [str(doc[i]).lower() for i in range(len(doc))]

pos = [doc[i].pos_ for i in range(len(doc))]


d = {'words' : words, 'pos' : pos}

df = pd.DataFrame(data = d)

sns.countplot(df.pos)

plt.show()
