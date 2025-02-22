import os

def get_file_size(file_path):
    """
    Get the size of a file in bytes.
    
    Args:
        file_path (str): Path to the file to check.
    
    Returns:
        int: Size of the file in bytes.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the path is a directory.
        PermissionError: If there's no permission to access the file.
    """
    return os.path.getsize(file_path)