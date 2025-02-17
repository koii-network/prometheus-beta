import os

def file_exists(file_path):
    """
    Check if a file exists at the given path.
    
    Args:
        file_path (str): The relative path to the file to check.
    
    Returns:
        bool: True if the file exists and is a file, False otherwise.
    """
    # Normalize the path to handle different path separators
    normalized_path = os.path.normpath(file_path)
    
    # Check if the path exists and is a file (not a directory)
    return os.path.isfile(normalized_path)