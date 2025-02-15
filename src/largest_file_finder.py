import os

def find_largest_file(directory='.'):
    """
    Find the largest file in the given directory.
    
    Args:
        directory (str, optional): Path to the directory to search. 
                                   Defaults to current directory.
    
    Returns:
        tuple: A tuple containing (largest file path, file size in bytes)
               Returns (None, 0) if no files are found
    
    Raises:
        NotADirectoryError: If the provided path is not a directory
    """
    # Validate input is a directory
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"{directory} is not a valid directory")
    
    largest_file = None
    largest_size = 0
    
    # Walk through all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip if it's a symlink or not a file
            if not os.path.isfile(file_path) or os.path.islink(file_path):
                continue
            
            try:
                # Get file size
                file_size = os.path.getsize(file_path)
                
                # Update largest file if current file is larger
                if file_size > largest_size:
                    largest_file = file_path
                    largest_size = file_size
            except (OSError, IOError):
                # Skip files that can't be accessed
                continue
    
    return largest_file, largest_size