import os
from typing import Optional
from datetime import datetime

def find_oldest_file(directory: str) -> Optional[str]:
    """
    Find the oldest file in a given directory.
    
    Args:
        directory (str): Path to the directory to search for the oldest file.
    
    Returns:
        Optional[str]: Path to the oldest file, or None if directory is empty or invalid.
    
    Raises:
        NotADirectoryError: If the provided path is not a directory.
    """
    # Validate input is a directory
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"The path {directory} is not a valid directory")
    
    # Get all files in the directory (excluding directories)
    files = [os.path.join(directory, f) for f in os.listdir(directory) 
             if os.path.isfile(os.path.join(directory, f))]
    
    # If no files, return None
    if not files:
        return None
    
    # Find the oldest file by creation time
    oldest_file = min(files, key=lambda f: os.path.getctime(f))
    
    return oldest_file