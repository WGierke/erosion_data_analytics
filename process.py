import os
import pandas as pd
from transformation import encode_onehot

def read_data() -> pd.DataFrame:
    """Read DataFrame"""
    file_path_full = os.getcwd() + '/data/processed.csv'

    if os.path.isfile(file_path_full):
        return pd.DataFrame.from_csv(file_path_full, sep=';')

def transform(df: pd.DataFrame) -> pd.DataFrame:
	"""Transform data"""
	df = encode_onehot(df, cols=['Rock type', 'Climate zone main'])
	return df

if __name__ == '__main__':
	data = read_data()
	data = transform(data)
	print(data)