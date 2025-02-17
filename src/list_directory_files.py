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
        NotADirectoryError: If the specified path is not a directory.
        FileNotFoundError: If the specified directory does not exist.
    """
    # Normalize the path to handle relative paths correctly
    full_path = os.path.abspath(directory_path)
    
    # Check if path exists and is a directory
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Directory not found: {full_path}")
    
    if not os.path.isdir(full_path):
        raise NotADirectoryError(f"Specified path is not a directory: {full_path}")
    
    # List all files in the directory (excluding subdirectories)
    return [f for f in os.listdir(full_path) if os.path.isfile(os.path.join(full_path, f))]