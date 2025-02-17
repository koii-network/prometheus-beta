import os

def delete_empty_directory(directory_path):
    """
    Delete an empty directory.
    
    Args:
        directory_path (str): Path to the directory to be deleted.
    
    Raises:
        OSError: If the directory is not empty or cannot be deleted.
        FileNotFoundError: If the directory does not exist.
    
    Returns:
        bool: True if the directory was successfully deleted.
    """
    # Check if directory exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory {directory_path} does not exist")
    
    # Check if it's a directory
    if not os.path.isdir(directory_path):
        raise OSError(f"{directory_path} is not a directory")
    
    # Check if directory is empty
    if os.listdir(directory_path):
        raise OSError(f"Directory {directory_path} is not empty")
    
    # Delete the empty directory
    os.rmdir(directory_path)
    return True