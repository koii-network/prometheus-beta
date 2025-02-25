import os
import shutil

def delete_directory(path):
    """
    Recursively delete a directory and all its contents.

    Args:
        path (str): The path to the directory to be deleted.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If the user lacks permissions to delete the directory.
        ValueError: If the path is not a directory.
        OSError: For other OS-related errors during deletion.
    """
    # Validate input type
    if not isinstance(path, str):
        raise TypeError(f"Path must be a string, not {type(path).__name__}")

    # Normalize the path to resolve any relative path components
    try:
        normalized_path = os.path.abspath(os.path.normpath(path))
    except Exception as e:
        raise ValueError(f"Invalid path: {e}")

    # Validate directory existence and type
    if not os.path.exists(normalized_path):
        raise FileNotFoundError(f"Directory not found: {normalized_path}")
    
    if not os.path.isdir(normalized_path):
        raise ValueError(f"Path is not a directory: {normalized_path}")

    # Additional safety check to prevent deleting root or system directories
    if normalized_path in ['/', '/home', '/etc', '/usr']:
        raise PermissionError(f"Cannot delete system directory: {normalized_path}")

    try:
        # Use shutil.rmtree for recursive directory deletion
        shutil.rmtree(normalized_path)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot delete directory {normalized_path}")
    except OSError as e:
        raise OSError(f"Error deleting directory {normalized_path}: {e}")
    
    # Verify deletion
    if os.path.exists(normalized_path):
        raise OSError(f"Failed to completely delete directory: {normalized_path}")

    return True  # Explicit confirmation of successful deletion