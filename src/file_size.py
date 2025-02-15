import os

def get_file_size(file_path):
    """
    Get the size of a given file in bytes.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        int: Size of the file in bytes.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the path is a directory.
        PermissionError: If there's no permission to access the file.
    """
    # Normalize the path to handle relative paths
    normalized_path = os.path.normpath(file_path)
    
    # Check if the file exists and is a file
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"File not found: {normalized_path}")
    
    if os.path.isdir(normalized_path):
        raise IsADirectoryError(f"Path is a directory, not a file: {normalized_path}")
    
    # Get and return the file size
    return os.path.getsize(normalized_path)