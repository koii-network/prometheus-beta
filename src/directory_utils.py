import os
from typing import List, Union

def list_files(directory: str) -> List[str]:
    """
    List all files in the specified directory.

    Args:
        directory (str): Path to the directory to list files from.

    Returns:
        List[str]: A list of filenames in the directory.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Expand any user-specific path (e.g., '~')
    full_path = os.path.expanduser(directory)

    # Validate the directory exists and is a directory
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Directory not found: {full_path}")
    
    if not os.path.isdir(full_path):
        raise NotADirectoryError(f"Specified path is not a directory: {full_path}")

    # List all files (excluding directories)
    return [f for f in os.listdir(full_path) if os.path.isfile(os.path.join(full_path, f))]