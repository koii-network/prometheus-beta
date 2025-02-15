import os

def calculate_directory_size(directory_path):
    """
    Calculate the total size of all files in the given directory.
    
    Args:
        directory_path (str): Path to the directory to calculate size for.
    
    Returns:
        int: Total size of all files in bytes.
    
    Raises:
        FileNotFoundError: If the directory does not exist.
        NotADirectoryError: If the path is not a directory.
    """
    # Validate directory path
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")
    
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"Path is not a directory: {directory_path}")
    
    # Initialize total size
    total_size = 0
    
    # Walk through directory and calculate file sizes
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Add file size to total
            total_size += os.path.getsize(file_path)
    
    return total_size