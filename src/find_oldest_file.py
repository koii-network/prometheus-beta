import os
from datetime import datetime

def find_oldest_file(directory):
    """
    Find the oldest file in the given directory.
    
    Args:
        directory (str): Path to the directory to search.
    
    Returns:
        str: Path to the oldest file, or None if directory is empty.
    
    Raises:
        FileNotFoundError: If the directory does not exist.
        NotADirectoryError: If the provided path is not a directory.
    """
    # Validate input directory
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Provided path is not a directory: {directory}")
    
    # Get all files in the directory
    files = [os.path.join(directory, f) for f in os.listdir(directory) 
             if os.path.isfile(os.path.join(directory, f))]
    
    # Return None if no files found
    if not files:
        return None
    
    # Find the oldest file based on creation time
    return min(files, key=os.path.getctime)