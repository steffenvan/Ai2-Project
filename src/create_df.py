import os

import pandas as pd


def create_df() :

    assert (os.path.exists("../data/similarities.pkl")==0), "sim DataFrame already exists"

    sim = pd.DataFrame()

    sim.to_pickle("../data/similarities.pkl")
