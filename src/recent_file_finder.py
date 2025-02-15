import os
from pathlib import Path
from typing import Union

def find_most_recent_file(directory: Union[str, Path]) -> Union[str, None]:
    """
    Find the most recently modified file in a given directory.
    
    Args:
        directory (str or Path): The directory to search for files.
    
    Returns:
        str or None: Path to the most recently modified file, or None if no files exist.
    """
    # Convert to Path object if string is provided
    directory = Path(directory)
    
    # Validate directory exists and is a directory
    if not directory.exists() or not directory.is_dir():
        raise ValueError(f"Invalid directory: {directory}")
    
    # Get all files in the directory
    files = [f for f in directory.iterdir() if f.is_file()]
    
    # If no files exist, return None
    if not files:
        return None
    
    # Find the most recently modified file
    most_recent_file = max(files, key=lambda f: f.stat().st_mtime)
    
    return str(most_recent_file)