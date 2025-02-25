import os

def create_directory(path):
    """
    Create a new directory at the specified path.
    
    Args:
        path (str): The path of the directory to create.
    
    Raises:
        FileExistsError: If the directory already exists.
        PermissionError: If there are insufficient permissions to create the directory.
    
    Returns:
        str: The absolute path of the created directory.
    """
    # Expand user and get absolute path
    abs_path = os.path.abspath(os.path.expanduser(path))
    
    # Check if directory already exists
    if os.path.exists(abs_path):
        raise FileExistsError(f"Directory already exists: {abs_path}")
    
    # Create directory
    os.makedirs(abs_path)
    
    return abs_path