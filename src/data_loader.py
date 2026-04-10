import pandas as pd
import zipfile

def load_from_zip(zip_path, internal_file_path):
    """
    zip_path: The full path to the .zip file (can be a string or Path object)
    internal_file_path: The path inside the zip (e.g., 'data/data_w_genres.csv')
    """
    # Open the zip file using the exact path provided
    with zipfile.ZipFile(zip_path, 'r') as z:
        with z.open(internal_file_path) as f:
            return pd.read_csv(f)