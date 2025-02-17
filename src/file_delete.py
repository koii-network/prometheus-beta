import os
import stat

def delete_file(file_path):
    """
    Delete a file from the specified path.
    
    Args:
        file_path (str): The relative path to the file to be deleted.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the user lacks permission to delete the file.
        IsADirectoryError: If the path is a directory instead of a file.
    """
    # Normalize the path to remove any potential relative path issues
    normalized_path = os.path.normpath(file_path)
    
    # Check if the file exists
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Check if it's a file (not a directory)
    if not os.path.isfile(normalized_path):
        raise IsADirectoryError(f"The path {file_path} is not a file.")
    
    # Get file stats
    try:
        file_stats = os.stat(normalized_path)
    except Exception as e:
        raise PermissionError(f"Cannot access file stats for {file_path}: {str(e)}")
    
    # Check if the file is writable by checking permissions
    if not bool(file_stats.st_mode & stat.S_IWUSR):
        raise PermissionError(f"Permission denied: Cannot delete {file_path}")
    
    # Attempt to delete the file
    try:
        os.remove(normalized_path)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot delete {file_path}")
    except Exception as e:
        raise PermissionError(f"Cannot delete {file_path}: {str(e)}")