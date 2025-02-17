import os
from typing import Optional

def find_most_recent_file(directory: str) -> Optional[str]:
    """
    Find the most recently modified file in a given directory.
    
    Args:
        directory (str): Path to the directory to search.
    
    Returns:
        Optional[str]: Relative path to the most recently modified file, 
                       or None if directory is empty or invalid.
    
    Raises:
        ValueError: If the provided path is not a directory.
    """
    # Validate input is a directory
    if not os.path.isdir(directory):
        raise ValueError(f"{directory} is not a valid directory")
    
    # Get list of files in the directory
    try:
        files = [os.path.join(directory, f) for f in os.listdir(directory) 
                 if os.path.isfile(os.path.join(directory, f))]
    except PermissionError:
        return None
    
    # If no files found, return None
    if not files:
        return None
    
    # Find the most recently modified file using modification time
    most_recent_file = max(files, key=os.path.getmtime)
    
    # Return relative path from the base directory
    return os.path.relpath(most_recent_file, start=directory)