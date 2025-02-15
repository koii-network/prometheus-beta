import os
import shutil

def move_file(source_path, destination_path):
    """
    Move a file from the source path to the destination path.
    
    Args:
        source_path (str): Relative path of the file to be moved
        destination_path (str): Relative path of the destination directory
    
    Raises:
        FileNotFoundError: If the source file does not exist
        IsADirectoryError: If the source path is a directory
        PermissionError: If there are permission issues
        ValueError: If source or destination paths are invalid
    """
    # Validate input paths
    if not source_path or not destination_path:
        raise ValueError("Source and destination paths must not be empty")
    
    # Convert to absolute paths 
    abs_source_path = os.path.abspath(source_path)
    abs_destination_path = os.path.abspath(destination_path)
    
    # Check if source file exists
    if not os.path.exists(abs_source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    # Check if source is a file, not a directory
    if not os.path.isfile(abs_source_path):
        raise IsADirectoryError(f"Source path must be a file: {source_path}")
    
    # Ensure destination directory exists, create if not
    os.makedirs(abs_destination_path, exist_ok=True)
    
    # Get filename from source path
    filename = os.path.basename(abs_source_path)
    destination_file_path = os.path.join(abs_destination_path, filename)
    
    try:
        # Move the file
        shutil.move(abs_source_path, destination_file_path)
    except PermissionError:
        raise PermissionError(f"Permission denied when moving file: {source_path}")
    
    return destination_file_path