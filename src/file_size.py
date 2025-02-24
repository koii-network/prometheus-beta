import os

def get_file_size(file_path):
    """
    Get the size of a file in bytes.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        int: Size of the file in bytes.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the path is a directory.
    """
    # Normalize the path to handle relative paths
    normalized_path = os.path.normpath(file_path)
    
    # Check if file exists
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"File not found: {normalized_path}")
    
    # Check if it's a file, not a directory
    if os.path.isdir(normalized_path):
        raise IsADirectoryError(f"Path is a directory, not a file: {normalized_path}")
    
    # Return file size in bytes
    return os.path.getsize(normalized_path)