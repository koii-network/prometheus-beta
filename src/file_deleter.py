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
    # Normalize the path to remove any relative path components
    normalized_path = os.path.normpath(file_path)
    
    # Check if the path exists
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"The file {normalized_path} does not exist.")
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(normalized_path):
        raise IsADirectoryError(f"The path {normalized_path} is not a file.")
    
    # Attempt to delete the file
    try:
        os.remove(normalized_path)
    except PermissionError:
        raise PermissionError(f"Permission denied: Unable to delete {normalized_path}")