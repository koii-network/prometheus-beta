import os

def get_file_size(file_path):
    """
    Get the size of a given file in bytes.
    
    Args:
        file_path (str): Path to the file whose size needs to be determined.
    
    Returns:
        int: Size of the file in bytes.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
        IsADirectoryError: If the specified path is a directory.
        PermissionError: If there's no permission to access the file.
    """
    # Validate input
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Get and return file size
    return os.path.getsize(file_path)