import os

def is_symbolic_link(path):
    """
    Detect whether the given path is a symbolic link.
    
    Args:
        path (str): The file path to check.
    
    Returns:
        bool: True if the path is a symbolic link, False otherwise.
    
    Raises:
        TypeError: If the path is not a string.
        ValueError: If the path is an empty string.
    """
    # Validate input
    if not isinstance(path, str):
        raise TypeError("Path must be a string")
    
    if not path:
        raise ValueError("Path cannot be an empty string")
    
    # Use os.path.islink to check if the path is a symbolic link
    return os.path.islink(path)