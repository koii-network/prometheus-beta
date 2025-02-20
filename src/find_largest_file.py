import os
import pathlib

def find_largest_file(directory):
    """
    Find the largest file in the given directory.
    
    Args:
        directory (str): Path to the directory to search.
    
    Returns:
        str: Path to the largest file, or None if no files found.
    
    Raises:
        ValueError: If the directory does not exist or is not a directory.
    """
    # Convert to absolute path and validate directory
    dir_path = pathlib.Path(directory).resolve()
    
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {directory}")
    
    if not dir_path.is_dir():
        raise ValueError(f"Path is not a directory: {directory}")
    
    # Find the largest file
    largest_file = None
    largest_size = 0
    
    for item in dir_path.iterdir():
        if item.is_file():
            file_size = item.stat().st_size
            if file_size > largest_size:
                largest_file = item
                largest_size = file_size
    
    # Return the path as a string for better compatibility
    return str(largest_file) if largest_file else None