import spacy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_pickle("../data/similarities.pkl")

sns.heatmap(df, annot = True)

plt.show()
