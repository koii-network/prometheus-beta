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
        bool: True if directory was successfully created.
    """
    try:
        # Use os.makedirs to create intermediate directories if they don't exist
        os.makedirs(path, exist_ok=False)
        return True
    except FileExistsError:
        # Raise if directory already exists (with exist_ok=False)
        raise FileExistsError(f"Directory '{path}' already exists.")
    except PermissionError:
        # Raise if insufficient permissions
        raise PermissionError(f"Permission denied: Cannot create directory '{path}'.")
    except Exception as e:
        # Catch any other unexpected errors
        raise OSError(f"Error creating directory: {str(e)}")