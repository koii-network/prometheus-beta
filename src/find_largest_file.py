import os

def find_largest_file(directory):
    """
    Find the largest file in the given directory.
    
    Args:
        directory (str): Path to the directory to search
    
    Returns:
        str: Path to the largest file, or None if directory is empty or invalid
    """
    # Validate input
    if not os.path.isdir(directory):
        return None
    
    # Initialize variables
    largest_file = None
    max_size = 0
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Check if it's a file (not a subdirectory)
        if os.path.isfile(filepath):
            file_size = os.path.getsize(filepath)
            
            # Update largest file if current file is larger
            if file_size > max_size:
                largest_file = filepath
                max_size = file_size
    
    return largest_file