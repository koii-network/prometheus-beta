import os

def find_largest_file(directory_path):
    """
    Find the largest file in the given directory.
    
    Args:
        directory_path (str): Path to the directory to search
    
    Returns:
        tuple: A tuple containing (largest file path, file size in bytes)
               Returns (None, 0) if no files are found or directory is invalid
    
    Raises:
        TypeError: If directory_path is not a string
        ValueError: If directory_path is an empty string
    """
    # Validate input
    if not isinstance(directory_path, str):
        raise TypeError("Directory path must be a string")
    
    if not directory_path:
        raise ValueError("Directory path cannot be an empty string")
    
    # Normalize the path and check if it exists
    try:
        directory_path = os.path.abspath(directory_path)
        
        if not os.path.isdir(directory_path):
            return None, 0
        
        # Initialize variables
        largest_file_path = None
        largest_file_size = 0
        
        # Iterate through all files in the directory
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            
            # Check if it's a file (not a subdirectory)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)
                
                # Update largest file if current file is larger
                if file_size > largest_file_size:
                    largest_file_path = file_path
                    largest_file_size = file_size
        
        return largest_file_path, largest_file_size
    
    except (OSError, PermissionError):
        # Handle potential errors like permission issues
        return None, 0