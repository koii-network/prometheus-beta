import os
import typing

def create_directory(path: str, mode: int = 0o755, parents: bool = False) -> bool:
    """
    Create a new directory with specified parameters.

    Args:
        path (str): The path of the directory to create.
        mode (int, optional): The file mode (permissions) for the new directory. 
                               Defaults to 0o755 (rwxr-xr-x).
        parents (bool, optional): If True, create parent directories as needed. 
                                  If False, will raise an error if parent directories 
                                  do not exist. Defaults to False.

    Returns:
        bool: True if directory was created successfully, False if directory already exists.

    Raises:
        PermissionError: If the user lacks permissions to create the directory.
        OSError: If there are issues creating the directory (e.g., invalid path).
    """
    try:
        # Validate input path
        if not isinstance(path, str) or not path:
            raise ValueError("Path must be a non-empty string")

        # Normalize the path to remove any trailing slashes or redundant separators
        normalized_path = os.path.normpath(path)

        # Check if directory already exists
        if os.path.exists(normalized_path):
            return False

        # Create directory with specified mode
        if parents:
            os.makedirs(normalized_path, mode=mode, exist_ok=False)
        else:
            os.mkdir(normalized_path, mode=mode)

        return True

    except FileExistsError:
        # This can happen even with exist_ok=False in some edge cases
        return False
    except PermissionError:
        # Re-raise with a clear error message
        raise PermissionError(f"Permission denied: Cannot create directory at {path}")
    except OSError as e:
        # Catch and potentially re-raise other OS-related errors
        raise OSError(f"Error creating directory {path}: {str(e)}")