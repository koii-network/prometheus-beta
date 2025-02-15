import os

def list_files(directory='.'):
    """
    List all files in a given directory.
    
    Args:
        directory (str, optional): Path to the directory to list files from. 
                                   Defaults to current directory.
    
    Returns:
        list: A list of file names in the specified directory.
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Validate the directory exists and is a directory
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Path is not a directory: {directory}")
    
    # List all files in the directory (excluding directories)
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]