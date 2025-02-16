import os

def file_exists(file_path):
    """
    Check if a file exists at the specified path.
    
    Args:
        file_path (str): Relative or absolute path to the file
    
    Returns:
        bool: True if the file exists, False otherwise
    """
    return os.path.isfile(file_path)