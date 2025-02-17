import os

def list_subdirectories(directory):
    """
    List all subdirectories in the given directory.
    
    Args:
        directory (str): Path to the directory to search for subdirectories
    
    Returns:
        list: A list of subdirectory names (full paths)
    
    Raises:
        FileNotFoundError: If the specified directory does not exist
        NotADirectoryError: If the specified path is not a directory
    """
    # Validate input directory exists and is a directory
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Path is not a directory: {directory}")
    
    # Use list comprehension to get full paths of subdirectories
    subdirs = [
        os.path.join(directory, item) 
        for item in os.listdir(directory) 
        if os.path.isdir(os.path.join(directory, item))
    ]
    
    return subdirs