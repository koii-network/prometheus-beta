import os

def rename_file(source_path, destination_path):
    """
    Rename a file from source path to destination path.
    
    Args:
        source_path (str): The current path of the file to be renamed.
        destination_path (str): The new path for the file.
    
    Raises:
        FileNotFoundError: If the source file does not exist.
        PermissionError: If there are insufficient permissions to rename the file.
        OSError: For other OS-related errors during file renaming.
    
    Returns:
        bool: True if the file was successfully renamed, False otherwise.
    """
    try:
        # Check if source file exists
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Source file not found: {source_path}")
        
        # Check if destination path already exists
        if os.path.exists(destination_path):
            raise FileExistsError(f"Destination file already exists: {destination_path}")
        
        # Rename the file
        os.rename(source_path, destination_path)
        return True
    
    except (FileNotFoundError, PermissionError, OSError) as e:
        # Re-raise the specific exception for better error handling
        raise