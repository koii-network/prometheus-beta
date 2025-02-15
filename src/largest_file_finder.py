import os

def find_largest_file(directory):
    """
    Find the largest file in the given directory.
    
    Args:
        directory (str): Path to the directory to search
    
    Returns:
        str: Path to the largest file, or None if directory is empty or invalid
    
    Raises:
        NotADirectoryError: If the provided path is not a directory
    """
    # Check if directory exists and is a directory
    if not os.path.exists(directory):
        return None
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"{directory} is not a valid directory")
    
    largest_file = None
    largest_size = 0
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Check if it's a file (not a subdirectory)
        if os.path.isfile(filepath):
            current_size = os.path.getsize(filepath)
            
            # Update largest file if current file is larger
            if current_size > largest_size:
                largest_file = filepath
                largest_size = current_size
    
    return largest_file