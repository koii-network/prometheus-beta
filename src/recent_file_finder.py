import os
from typing import Optional, Union


def find_most_recent_file(directory: Union[str, os.PathLike]) -> Optional[str]:
    """
    Find the most recently modified file in the specified directory.

    Args:
        directory (str or os.PathLike): Path to the directory to search.

    Returns:
        Optional[str]: Path to the most recently modified file, 
                       or None if the directory is empty or does not exist.

    Raises:
        TypeError: If the directory is not a string or path-like object.
        NotADirectoryError: If the provided path is not a directory.
    """
    # Validate input
    if not isinstance(directory, (str, os.PathLike)):
        raise TypeError("Directory must be a string or path-like object")
    
    # Convert to absolute path and check if it's a directory
    dir_path = os.path.abspath(directory)
    if not os.path.isdir(dir_path):
        raise NotADirectoryError(f"{dir_path} is not a valid directory")
    
    # Get all files in the directory
    try:
        files = [
            os.path.join(dir_path, f) 
            for f in os.listdir(dir_path) 
            if os.path.isfile(os.path.join(dir_path, f))
        ]
    except PermissionError:
        return None
    
    # If no files, return None
    if not files:
        return None
    
    # Find the most recently modified file
    return max(files, key=os.path.getmtime)