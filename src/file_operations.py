import os

def delete_file(file_path):
    """
    Delete a file at the specified path.
    
    Args:
        file_path (str): The path to the file to be deleted.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the user lacks permission to delete the file.
        IsADirectoryError: If the path is a directory instead of a file.
    """
    # Validate input is a string
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(file_path):
        raise IsADirectoryError(f"Path is not a file: {file_path}")
    
    # Attempt to delete the file
    try:
        os.remove(file_path)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot delete {file_path}")