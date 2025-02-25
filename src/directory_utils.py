import os
import typing

def create_directory(path: str, exist_ok: bool = False) -> typing.Optional[str]:
    """
    Create a new directory at the specified path.

    Args:
        path (str): The path where the directory should be created.
        exist_ok (bool, optional): If True, do not raise an error if the directory already exists. 
                                   Defaults to False.

    Returns:
        Optional[str]: The absolute path of the created directory, or None if creation fails.

    Raises:
        PermissionError: If the user lacks permission to create the directory.
        OSError: For other OS-related errors during directory creation.
    """
    try:
        # Expand and normalize the path
        abs_path = os.path.abspath(os.path.expanduser(path))
        
        # Validate input
        if not isinstance(path, str):
            raise TypeError("Path must be a string")
        
        if not path.strip():
            raise ValueError("Path cannot be an empty string")
        
        # Create directory
        os.makedirs(abs_path, exist_ok=exist_ok)
        
        return abs_path
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot create directory at {path}")
    except FileExistsError:
        if not exist_ok:
            raise
        return abs_path
    except OSError as e:
        raise OSError(f"Failed to create directory at {path}: {str(e)}")