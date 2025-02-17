import os

def list_subdirectories(directory_path):
    """
    List all subdirectories in the given directory.
    
    Args:
        directory_path (str): Path to the directory to list subdirectories from
    
    Returns:
        list: A list of subdirectory names (not full paths)
    
    Raises:
        FileNotFoundError: If the specified directory does not exist
        NotADirectoryError: If the specified path is not a directory
    """
    # Validate input 
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Specified path is not a directory: {directory_path}")
    
    # List comprehension to get only subdirectories
    subdirs = [
        item for item in os.listdir(directory_path) 
        if os.path.isdir(os.path.join(directory_path, item))
    ]
    
    return subdirs