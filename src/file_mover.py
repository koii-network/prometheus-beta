import os
import shutil

def move_file(source_path, destination_dir):
    """
    Move a file from the source path to the specified destination directory.
    
    Args:
        source_path (str): The relative path to the source file to be moved.
        destination_dir (str): The relative path to the destination directory.
    
    Raises:
        FileNotFoundError: If the source file does not exist.
        NotADirectoryError: If the destination is not a directory.
        PermissionError: If there are insufficient permissions to move the file.
        IOError: For other IO-related errors during file movement.
    
    Returns:
        str: The new path of the moved file.
    """
    # Normalize paths to handle different path separators
    source_path = os.path.normpath(source_path)
    destination_dir = os.path.normpath(destination_dir)
    
    # Check if source file exists
    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    # Check if destination is a directory
    if not os.path.isdir(destination_dir):
        raise NotADirectoryError(f"Destination is not a directory: {destination_dir}")
    
    # Get the filename from the source path
    filename = os.path.basename(source_path)
    
    # Construct the destination path
    destination_path = os.path.join(destination_dir, filename)
    
    try:
        # Move the file
        shutil.move(source_path, destination_path)
        return destination_path
    except PermissionError:
        raise PermissionError(f"Permission denied when moving file from {source_path} to {destination_dir}")
    except IOError as e:
        raise IOError(f"Error moving file: {e}")