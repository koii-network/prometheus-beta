import os

def list_directory_files(directory_path):
    """
    List all files in the specified directory.
    
    Args:
        directory_path (str): Path to the directory to list files from.
    
    Returns:
        list: A sorted list of filenames in the directory.
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Use os.path to validate and process the directory path
    full_path = os.path.abspath(directory_path)
    
    # Validate directory exists
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Directory not found: {full_path}")
    
    # Validate it's a directory
    if not os.path.isdir(full_path):
        raise NotADirectoryError(f"Path is not a directory: {full_path}")
    
    # List only files (not subdirectories), using relative paths
    files = [f for f in os.listdir(full_path) if os.path.isfile(os.path.join(full_path, f))]
    
    # Return sorted list of files for consistent output
    return sorted(files)