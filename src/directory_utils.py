import os
from typing import List, Optional


def list_subdirectories(directory_path: str) -> List[str]:
    """
    List all subdirectories in the given directory.

    Args:
        directory_path (str): The path to the directory to list subdirectories from.

    Returns:
        List[str]: A list of subdirectory names (not full paths).

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
        PermissionError: If there are insufficient permissions to access the directory.
    """
    # Normalize the path to handle different path formats
    normalized_path = os.path.normpath(directory_path)

    # Check if the directory exists
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"The directory {normalized_path} does not exist.")

    # Check if the path is a directory
    if not os.path.isdir(normalized_path):
        raise NotADirectoryError(f"{normalized_path} is not a directory.")

    try:
        # List all entries in the directory and filter for subdirectories
        subdirs = [
            entry.name 
            for entry in os.scandir(normalized_path) 
            if entry.is_dir()
        ]
        return sorted(subdirs)
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing {normalized_path}")