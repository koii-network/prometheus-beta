import os

def check_directory_exists(directory_path):
    """
    Check if a directory exists.
    
    Args:
        directory_path (str): The path to the directory to check.
    
    Returns:
        bool: True if the directory exists, False otherwise.
    """
    return os.path.isdir(directory_path)