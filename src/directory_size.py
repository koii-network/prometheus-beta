import os

def calculate_directory_size(directory_path):
    """
    Calculate the total size of all files in a given directory.
    
    Args:
        directory_path (str): Path to the directory to calculate size for.
    
    Returns:
        int: Total size of all files in the directory in bytes.
    
    Raises:
        FileNotFoundError: If the directory does not exist.
        NotADirectoryError: If the path is not a directory.
    """
    # Validate input directory
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")
    
    total_size = 0
    
    # Walk through all files in the directory
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Add the size of each file
            total_size += os.path.getsize(file_path)
    
    return total_size