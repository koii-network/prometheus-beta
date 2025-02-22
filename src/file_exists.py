import os

def is_file_exists(file_path: str) -> bool:
    """
    Check if a file exists at the given path.
    
    Args:
        file_path (str): Relative path to the file to check
    
    Returns:
        bool: True if the file exists, False otherwise
    """
    return os.path.isfile(file_path)