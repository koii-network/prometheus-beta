import os
import pathlib

def find_largest_file(directory_path):
    """
    Find the largest file in the given directory.
    
    Args:
        directory_path (str): Path to the directory to search.
    
    Returns:
        tuple: A tuple containing (largest file path, file size in bytes)
               Returns (None, 0) if no files are found.
    
    Raises:
        ValueError: If the directory path is invalid or not a directory.
    """
    # Validate input
    dir_path = pathlib.Path(directory_path)
    
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {directory_path}")
    
    if not dir_path.is_dir():
        raise ValueError(f"Provided path is not a directory: {directory_path}")
    
    # Initialize variables
    largest_file = None
    largest_size = 0
    
    # Iterate through all files in the directory
    for entry in dir_path.iterdir():
        if entry.is_file():
            try:
                file_size = entry.stat().st_size
                if file_size > largest_size:
                    largest_file = entry
                    largest_size = file_size
            except Exception:
                # Skip files that can't be accessed
                continue
    
    # Return the result
    return (str(largest_file) if largest_file else None, largest_size)