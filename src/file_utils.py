import os

def file_exists(file_path: str) -> bool:
    """
    Check if a file exists at the given path.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file exists and is a file, False otherwise.

    Raises:
        TypeError: If the file_path is not a string.
    """
    # Validate input type
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")
    
    # Normalize the path and check if it exists and is a file
    return os.path.isfile(os.path.expanduser(file_path))