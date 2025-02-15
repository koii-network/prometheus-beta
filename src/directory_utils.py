import os

def directory_exists(path):
    """
    Check if a directory exists.
    
    Args:
        path (str): The path to the directory to check.
    
    Returns:
        bool: True if the directory exists and is a directory, False otherwise.
    """
    return os.path.exists(path) and os.path.isdir(path)