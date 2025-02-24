import os
import pathlib

def find_largest_file(directory):
    """
    Find the largest file in a given directory.

    Args:
        directory (str): Path to the directory to search.

    Returns:
        str: Absolute path to the largest file in the directory.
        None: If the directory is empty or no files exist.

    Raises:
        ValueError: If the directory does not exist or is not a directory.
        PermissionError: If there are permission issues accessing the directory.
    """
    # Validate input directory
    dir_path = pathlib.Path(directory).resolve()
    
    if not dir_path.exists():
        raise ValueError(f"Directory does not exist: {dir_path}")
    
    if not dir_path.is_dir():
        raise ValueError(f"Provided path is not a directory: {dir_path}")
    
    # Find the largest file
    try:
        # Use generator to efficiently find largest file
        largest_file = max(
            (f for f in dir_path.iterdir() if f.is_file()),
            key=lambda x: x.stat().st_size,
            default=None
        )
        
        # Return absolute path of largest file or None if no files
        return str(largest_file) if largest_file else None
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing directory: {dir_path}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error finding largest file: {e}")