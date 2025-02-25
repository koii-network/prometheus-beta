import os
from typing import List


def list_subdirectories(directory_path: str) -> List[str]:
    """
    List all subdirectories in a given directory.

    Args:
        directory_path (str): Path to the directory to search for subdirectories.

    Returns:
        List[str]: A list of subdirectory names.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Check if the path exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")

    # Check if the path is a directory
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")

    # Get all subdirectories
    try:
        # List all entries in the directory and filter for directories
        subdirectories = [
            name for name in os.listdir(directory_path) 
            if os.path.isdir(os.path.join(directory_path, name))
        ]
        return subdirectories
    except PermissionError:
        # Handle permission issues
        raise PermissionError(f"Permission denied to access directory: {directory_path}")