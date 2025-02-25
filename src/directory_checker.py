import os
from typing import Union, Optional


def check_directory_exists(path: Union[str, os.PathLike]) -> bool:
    """
    Check if a directory exists at the specified path.

    Args:
        path (Union[str, os.PathLike]): The path to the directory to check.

    Returns:
        bool: True if the directory exists, False otherwise.

    Raises:
        TypeError: If the path is None or not a string/path-like object.
    """
    # Check for None or invalid input
    if path is None:
        raise TypeError("Path cannot be None")
    
    # Expand user and normalize the path
    expanded_path = os.path.expanduser(path)
    
    # Check if the path exists and is a directory
    return os.path.isdir(expanded_path)