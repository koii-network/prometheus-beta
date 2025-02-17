import os
from typing import List

def list_subdirectories(directory_path: str) -> List[str]:
    """
    List all subdirectories in the given directory.
    
    Args:
        directory_path (str): Path to the directory to search for subdirectories.
    
    Returns:
        List[str]: A list of subdirectory names (full paths).
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Validate input directory
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")
    
    # List all subdirectories (full paths)
    subdirs = [
        os.path.join(directory_path, d) 
        for d in os.listdir(directory_path) 
        if os.path.isdir(os.path.join(directory_path, d))
    ]
    
    return subdirs