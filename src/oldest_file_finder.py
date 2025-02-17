import os
from typing import Optional, Union

def find_oldest_file(directory: Union[str, os.PathLike]) -> Optional[str]:
    """
    Find the oldest file in a given directory.
    
    Args:
        directory (str or os.PathLike): Path to the directory to search
    
    Returns:
        Optional[str]: Relative path to the oldest file, or None if directory is empty or invalid
    
    Raises:
        NotADirectoryError: If the provided path is not a directory
    """
    # Validate input
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"{directory} is not a valid directory")
    
    # Get all files in the directory (excluding subdirectories)
    files = [os.path.join(directory, f) for f in os.listdir(directory) 
             if os.path.isfile(os.path.join(directory, f))]
    
    # Return None if no files found
    if not files:
        return None
    
    # Find the oldest file by creation time
    oldest_file = min(files, key=os.path.getctime)
    
    # Return relative path
    return os.path.relpath(oldest_file)