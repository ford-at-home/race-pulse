import pandas as pd

def preprocess_data(df):
    df = df.set_index('timestamp')
    df = df.sort_index()
    return df
