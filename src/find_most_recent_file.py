import os
from typing import Optional

def find_most_recent_file(directory: str = '.') -> Optional[str]:
    """
    Find the most recently modified file in the given directory.
    
    Args:
        directory (str, optional): Path to the directory to search. Defaults to current directory.
    
    Returns:
        Optional[str]: Path to the most recently modified file, or None if no files found.
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
    """
    # Check if directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    # Check if directory is actually a directory
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Provided path is not a directory: {directory}")
    
    # List all files in the directory
    files = [os.path.join(directory, f) for f in os.listdir(directory) 
             if os.path.isfile(os.path.join(directory, f))]
    
    # If no files found, return None
    if not files:
        return None
    
    # Find the most recently modified file
    return max(files, key=os.path.getmtime)