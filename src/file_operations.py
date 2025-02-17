import os
import shutil

def move_file(source_path, destination_path):
    """
    Move a file from source path to destination path.
    
    Args:
        source_path (str): The current path of the file to be moved.
        destination_path (str): The target path where the file should be moved.
    
    Raises:
        FileNotFoundError: If the source file does not exist.
        IsADirectoryError: If the source path is a directory.
        PermissionError: If there are insufficient permissions to move the file.
        OSError: For other OS-related errors during file movement.
    
    Returns:
        str: The new path of the moved file.
    """
    # Normalize paths to handle relative paths consistently
    source_path = os.path.normpath(source_path)
    destination_path = os.path.normpath(destination_path)
    
    # Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    # Check if source is a file, not a directory
    if os.path.isdir(source_path):
        raise IsADirectoryError(f"Source path is a directory, not a file: {source_path}")
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    
    try:
        # Move the file
        shutil.move(source_path, destination_path)
        return destination_path
    except PermissionError:
        raise PermissionError(f"Permission denied when moving file from {source_path} to {destination_path}")
    except OSError as e:
        raise OSError(f"Error moving file: {e}")