import spacy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_pickle("../data/frames.pkl")

print(df.head(20))
