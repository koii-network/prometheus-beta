import os
from typing import Union, Optional

def check_directory_exists(path: Union[str, os.PathLike]) -> bool:
    """
    Check if a directory exists at the specified path.

    Args:
        path (str or os.PathLike): The path to the directory to check.

    Returns:
        bool: True if the path exists and is a directory, False otherwise.

    Raises:
        TypeError: If the path is not a string or path-like object.
    """
    try:
        # Expand user home directory and normalize the path
        expanded_path = os.path.expanduser(path)
        normalized_path = os.path.normpath(expanded_path)

        # Check if path exists and is a directory
        return os.path.isdir(normalized_path)
    except TypeError:
        # Raise a more informative error if an invalid path type is provided
        raise TypeError("Path must be a string or path-like object")