import os
from typing import List, Union

def list_directory_files(directory_path: str) -> List[str]:
    """
    List all files in a given directory.

    Args:
        directory_path (str): Path to the directory to list files from.

    Returns:
        List[str]: A list of filenames in the directory.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
        PermissionError: If there are insufficient permissions to access the directory.
    """
    # Validate input
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory {directory_path} does not exist.")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"The path {directory_path} is not a directory.")
    
    try:
        # List only files, not subdirectories
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return files
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to access directory {directory_path}")