"""
Data Loading Module for Spotify Analysis

This module handles loading and basic validation of Spotify data
Functions here should be reusable across multiple notebooks
"""

import pandas as pd
import zipfile
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def load_from_zip(zip_file_name: str, file_name: str):
    """
    Load CSV file from inside a zip without extraction
    """
    # Get path relative to project root
    zip_path = Path(__file__).parent.parent / 'data' / zip_file_name

    with zipfile.ZipFile(zip_path, 'r') as z:
        with z.open(f'data/{file_name}') as f:  # ← ADD 'data/' HERE
            df = pd.read_csv(f)
            logger.info(f"Loaded {file_name} - {df.shape[0]} rows, {df.shape[1]} columns")
            return df