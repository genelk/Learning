import pandas as pd
import os

def load_csv_data(file_path: str):
    if not os.path.exists(file_path):
        print(f"Error: The file at {file_path} was not found!")
        return None
    try:
        print(f"Loading data from {file_path}...")
        df = pd.read_csv(file_path)
        print(f"Success! Loaded {len(df)} rows.")
        return df
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return None

spotify_df = load_csv_data(r"path/to/your/data.csv")

if spotify_df is not None:
    print(spotify_df.head())