import os
import errno

def create_directory(path):
    """
    Create a new directory at the specified path.
    
    Args:
        path (str): The path of the directory to create.
    
    Raises:
        OSError: If the directory cannot be created due to permission issues 
                 or if the directory already exists.
    
    Returns:
        str: The absolute path of the created directory.
    """
    try:
        # Resolve the absolute path and handle relative paths
        abs_path = os.path.abspath(path)
        
        # Create the directory with appropriate permissions
        # exist_ok=False ensures an error is raised if directory exists
        os.makedirs(abs_path, exist_ok=False, mode=0o755)
        
        return abs_path
    except FileExistsError:
        raise OSError(f"Directory already exists: {path}")
    except PermissionError:
        raise OSError(f"Permission denied when creating directory: {path}")