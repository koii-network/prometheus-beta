import os
from typing import List, Optional

def list_subdirectories(directory_path: str) -> List[str]:
    """
    List all subdirectories in a given directory.

    Args:
        directory_path (str): Path to the directory to search for subdirectories.

    Returns:
        List[str]: A list of subdirectory names (not full paths).

    Raises:
        ValueError: If the provided path is not a directory.
        FileNotFoundError: If the directory does not exist.
    """
    # Check if the path exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    # Check if the path is a directory
    if not os.path.isdir(directory_path):
        raise ValueError(f"Provided path is not a directory: {directory_path}")
    
    # List and filter only subdirectories
    try:
        subdirs = [
            entry.name 
            for entry in os.scandir(directory_path) 
            if entry.is_dir()
        ]
        return subdirs
    except PermissionError:
        raise PermissionError(f"Permission denied to access directory: {directory_path}")