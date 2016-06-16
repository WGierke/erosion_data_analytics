import os
import pandas as pd

processed_file = '/data/processed.csv'

def processed_data() -> pd.DataFrame:
    """Create or read DataFrame"""
    file_path_full = os.getcwd() + processed_file

    if os.path.isfile(file_path_full):
        return pd.DataFrame.from_csv(file_path_full, sep=';')

if __name__ == '__main__':
	data = processed_data()
	print(data)