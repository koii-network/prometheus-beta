import os

def get_file_size(file_path):
    """
    Get the size of a file in bytes.
    
    Args:
        file_path (str): Path to the file whose size needs to be determined.
    
    Returns:
        int: Size of the file in bytes.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the path is a directory instead of a file.
        PermissionError: If there are insufficient permissions to access the file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    if os.path.isdir(file_path):
        raise IsADirectoryError(f"{file_path} is a directory, not a file.")
    
    return os.path.getsize(file_path)