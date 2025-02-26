import os

def count_files_in_directory(directory_path):
    """
    Count the number of files in a given directory.
    
    Args:
        directory_path (str): Path to the directory to count files in.
    
    Returns:
        int: Number of files in the directory.
    
    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Validate directory exists and is a directory
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")
    
    # Count files (not including subdirectories)
    return len([f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))])