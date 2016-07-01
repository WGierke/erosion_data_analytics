import os
import pandas as pd
import numpy as np
from transformation import encode_onehot

def read_data() -> pd.DataFrame:
    """Read DataFrame"""
    file_path_full = os.getcwd() + '/data/processed.csv'

    if os.path.isfile(file_path_full):
        return pd.read_csv(file_path_full, sep=';')

def clean(df: pd.DataFrame) -> pd.DataFrame:
    #Remove invalid characters
    df["Mean basin elevation (m)"] = df["Mean basin elevation (m)"].apply(lambda x: str(x).replace('--', '-1'))
    df["Basin Relief (m)"] = df["Basin Relief (m)"].apply(lambda x: str(x).replace('--', '-1'))
    df["Mean Basin slope"] = df["Mean Basin slope"].apply(lambda x: str(x).replace('o', '0'))
    df["Seismic regime"] = df["Seismic regime"].apply(lambda x: '1' if x == 'Yes' else '0')

    #Cast all numbers to floats
    exclude_columns = set(["Unamed: 0", "Paper", "Name", "Rock type", "Climate zone main"])
    cast_columns = set(df.columns.values) - exclude_columns
    for col in cast_columns:
        df[col] = df[col].apply(lambda x : str(x).replace(',', '.')).astype(np.float)
    return df

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Transform data"""
    df = encode_onehot(df, cols=['Rock type', 'Climate zone main'])
    return df

def get_processed_data() -> pd.DataFrame:
    data = read_data()
    data = clean(data)
    data = transform(data)
    return data

if __name__ == '__main__':
    print(get_processed_data())