import os

def list_directory_files(directory_path='.'):
    """
    List all files in a given directory.
    
    Args:
        directory_path (str, optional): Path to the directory to list files from. 
                                        Defaults to current directory ('.').
    
    Returns:
        list: A list of filenames (not full paths) in the specified directory.
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Validate the directory exists and is a directory
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Specified path is not a directory: {directory_path}")
    
    # List all files in the directory (not including subdirectories)
    return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]