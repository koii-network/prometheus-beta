import os
from typing import Optional
from datetime import datetime

def find_oldest_file(directory: str = '.') -> Optional[str]:
    """
    Find the oldest file in a given directory.
    
    Args:
        directory (str, optional): Path to the directory to search. Defaults to current directory.
    
    Returns:
        Optional[str]: Path to the oldest file, or None if no files are found.
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
    """
    # Validate directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    # Ensure it's a directory
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Path is not a directory: {directory}")
    
    # Get all files in the directory
    files = [
        os.path.join(directory, f) for f in os.listdir(directory) 
        if os.path.isfile(os.path.join(directory, f))
    ]
    
    # Return None if no files found
    if not files:
        return None
    
    # Find the oldest file based on creation time
    return min(files, key=lambda f: os.path.getctime(f))