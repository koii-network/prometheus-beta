import os

def delete_empty_directory(path):
    """
    Deletes an empty directory.
    
    Args:
        path (str): Path to the directory to be deleted.
    
    Raises:
        FileNotFoundError: If the directory does not exist.
        OSError: If the directory is not empty or cannot be deleted.
    """
    # Validate that path exists
    if not os.path.exists(path):
        raise FileNotFoundError(f"Directory not found: {path}")
    
    # Validate it's a directory
    if not os.path.isdir(path):
        raise OSError(f"Path is not a directory: {path}")
    
    # Check if directory is empty
    if os.listdir(path):
        raise OSError(f"Directory is not empty: {path}")
    
    # Delete the empty directory
    os.rmdir(path)