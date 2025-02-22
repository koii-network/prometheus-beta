import os

def count_files_in_directory(directory_path='.'):
    """
    Count the number of files in a given directory.
    
    Args:
        directory_path (str, optional): Path to the directory to count files in. 
                                        Defaults to current directory ('.').
    
    Returns:
        int: Number of files in the directory.
    
    Raises:
        FileNotFoundError: If the directory does not exist.
        NotADirectoryError: If the path is not a directory.
    """
    # Normalize the path to handle relative paths
    full_path = os.path.abspath(directory_path)
    
    # Check if path exists
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    # Check if path is a directory
    if not os.path.isdir(full_path):
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")
    
    # Count files (not directories)
    return len([f for f in os.listdir(full_path) if os.path.isfile(os.path.join(full_path, f))])