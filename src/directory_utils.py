import os

def list_directory_files(directory_path='.'):
    """
    List all files in the specified directory.
    
    Args:
        directory_path (str, optional): Path to the directory to list files from. 
                                        Defaults to current directory.
    
    Returns:
        list: A list of filenames (not full paths) in the specified directory.
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Normalize the path to handle relative paths
    full_path = os.path.abspath(directory_path)
    
    # Check if the path exists
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    # Check if it's a directory
    if not os.path.isdir(full_path):
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")
    
    # List only files (not directories)
    return [f for f in os.listdir(full_path) if os.path.isfile(os.path.join(full_path, f))]