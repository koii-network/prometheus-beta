import os

def file_exists(file_path):
    """
    Check if a file exists at the given path.
    
    Args:
        file_path (str): Relative or absolute path to the file.
    
    Returns:
        bool: True if the file exists and is a file, False otherwise.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    return os.path.isfile(file_path)