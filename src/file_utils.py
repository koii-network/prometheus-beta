import os

def file_exists(file_path):
    """
    Check if a file exists at the specified path.
    
    Args:
        file_path (str): The path to the file to check.
    
    Returns:
        bool: True if the file exists and is a file, False otherwise.
    """
    return os.path.isfile(file_path)