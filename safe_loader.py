import pandas as pd
import zipfile

def load_from_zip(zip_path: str, file_name: str):
    """
    Load CSV file from inside a zip without extraction
    """
    with zipfile.ZipFile(zip_path, 'r') as z:
        with z.open(file_name) as f:
            df = pd.read_csv(f)
            print(f"Loaded {file_name} - {df.shape[0]} rows, {df.shape[1]} columns")
            return df