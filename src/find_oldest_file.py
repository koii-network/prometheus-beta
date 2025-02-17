import os
from typing import Optional

def find_oldest_file(directory: str) -> Optional[str]:
    """
    Find the oldest file in the given directory.
    
    Args:
        directory (str): Path to the directory to search
    
    Returns:
        Optional[str]: Path to the oldest file, or None if directory is empty or invalid
    """
    # Validate directory input
    if not os.path.isdir(directory):
        return None
    
    # Get all files in the directory (excluding subdirectories)
    files = [os.path.join(directory, f) for f in os.listdir(directory) 
             if os.path.isfile(os.path.join(directory, f))]
    
    # If no files found, return None
    if not files:
        return None
    
    # Find the file with the oldest creation time
    oldest_file = min(files, key=os.path.getctime)
    
    return oldest_file