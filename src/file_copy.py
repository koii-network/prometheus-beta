import os
import shutil

def copy_file(source_path, destination_path):
    """
    Copy a file from source location to destination location.
    
    Args:
        source_path (str): Path to the source file to be copied.
        destination_path (str): Path where the file should be copied to.
    
    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are permission issues during copying.
        IsADirectoryError: If source path is a directory instead of a file.
    """
    # Validate source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    # Validate source is a file, not a directory
    if not os.path.isfile(source_path):
        raise IsADirectoryError(f"Source path is not a file: {source_path}")
    
    # Ensure destination directory exists
    destination_dir = os.path.dirname(destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)
    
    try:
        # Use shutil for cross-platform file copying
        shutil.copy2(source_path, destination_path)
    except PermissionError:
        raise PermissionError(f"Permission denied when copying from {source_path} to {destination_path}")