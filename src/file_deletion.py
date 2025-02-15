import os

def delete_file(file_path):
    """
    Delete a file at the specified path.
    
    Args:
        file_path (str): Relative path to the file to be deleted.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the user lacks permission to delete the file.
        IsADirectoryError: If the path is a directory instead of a file.
    """
    # Normalize the path to handle potential '..' or './' in the path
    normalized_path = os.path.normpath(file_path)
    
    # Check if the file exists
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"File not found: {normalized_path}")
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(normalized_path):
        raise IsADirectoryError(f"Path is not a file: {normalized_path}")
    
    # Attempt to delete the file
    try:
        os.remove(normalized_path)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot delete {normalized_path}")