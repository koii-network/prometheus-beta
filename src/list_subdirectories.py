import os

def list_subdirectories(directory_path):
    """
    List all subdirectories in a given directory.
    
    Args:
        directory_path (str): Path to the directory to search for subdirectories.
    
    Returns:
        list: A list of subdirectory names (not full paths).
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Validate input directory
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")
    
    # List all subdirectories
    try:
        subdirs = [
            item for item in os.listdir(directory_path) 
            if os.path.isdir(os.path.join(directory_path, item))
        ]
        return subdirs
    except PermissionError:
        raise PermissionError(f"Permission denied to access directory: {directory_path}")