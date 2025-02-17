import os

def find_largest_file(directory):
    """
    Find the largest file in the given directory.
    
    Args:
        directory (str): Path to the directory to search.
    
    Returns:
        str: Full path to the largest file, or None if no files found.
    
    Raises:
        FileNotFoundError: If the directory does not exist.
        NotADirectoryError: If the provided path is not a directory.
    """
    # Validate input directory
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Path is not a directory: {directory}")
    
    # Initialize variables
    largest_file = None
    max_size = 0
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Only consider files (not directories)
        if os.path.isfile(filepath):
            file_size = os.path.getsize(filepath)
            
            # Update largest file if current file is larger
            if file_size > max_size:
                max_size = file_size
                largest_file = filepath
    
    return largest_file