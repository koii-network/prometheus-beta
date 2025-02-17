import os

def file_exists(file_path):
    """
    Check if a file exists at the given path.
    
    Args:
        file_path (str): Relative or absolute path to the file.
    
    Returns:
        bool: True if the file exists and is a file, False otherwise.
    """
    return os.path.isfile(file_path)