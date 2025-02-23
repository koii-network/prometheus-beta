import os

def file_exists(file_path):
    """
    Check if a file exists at the given path.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file exists and is a file, False otherwise.

    Raises:
        TypeError: If the file_path is not a string.
    """
    # Check if input is a string
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Normalize the path to handle different path separators
    normalized_path = os.path.normpath(file_path)
    
    # Check if path exists and is a file (not a directory)
    return os.path.isfile(normalized_path)