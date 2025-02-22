import os

def find_largest_file(directory_path):
    """
    Find the largest file in the given directory.
    
    Args:
        directory_path (str): Path to the directory to search.
    
    Returns:
        tuple: A tuple containing (largest_file_path, file_size_in_bytes)
               Returns (None, 0) if no files are found or directory is empty.
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Validate input
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Specified path is not a directory: {directory_path}")
    
    # Initialize variables
    largest_file = None
    largest_size = 0
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        # Skip directories
        if os.path.isfile(file_path):
            current_size = os.path.getsize(file_path)
            
            # Update largest file if current file is larger
            if current_size > largest_size:
                largest_file = file_path
                largest_size = current_size
    
    return largest_file, largest_size