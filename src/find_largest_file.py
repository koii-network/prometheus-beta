import os

def find_largest_file(directory):
    """
    Find the largest file in a given directory.
    
    Args:
        directory (str): Path to the directory to search
    
    Returns:
        str: Path to the largest file, or None if directory is empty or invalid
    
    Raises:
        ValueError: If directory is not a valid directory
    """
    # Validate directory
    if not os.path.isdir(directory):
        raise ValueError(f"Invalid directory: {directory}")
    
    # Initialize variables
    largest_file = None
    max_size = 0
    
    # Walk through directory and find largest file
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
                if file_size > max_size:
                    max_size = file_size
                    largest_file = file_path
            except OSError:
                # Skip files that can't be accessed
                continue
    
    return largest_file