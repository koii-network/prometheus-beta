import os
import stat

def get_file_permissions(file_path):
    """
    Get the file permissions of a given file.

    Args:
        file_path (str): Path to the file whose permissions are to be retrieved.

    Returns:
        dict: A dictionary containing file permission details:
            - 'mode': Numeric permission mode (e.g., 0o755)
            - 'readable': Boolean indicating if file is readable
            - 'writable': Boolean indicating if file is writable
            - 'executable': Boolean indicating if file is executable
            - 'permission_string': Symbolic representation of permissions (e.g., 'rwxr-xr-x')

    Raises:
        FileNotFoundError: If the specified file does not exist
        PermissionError: If access to file information is denied
    """
    try:
        # Get file status
        file_stat = os.stat(file_path)
        mode = file_stat.st_mode

        # Create permission string
        permission_string = ''
        permission_string += 'r' if mode & stat.S_IRUSR else '-'
        permission_string += 'w' if mode & stat.S_IWUSR else '-'
        permission_string += 'x' if mode & stat.S_IXUSR else '-'
        permission_string += 'r' if mode & stat.S_IRGRP else '-'
        permission_string += 'w' if mode & stat.S_IWGRP else '-'
        permission_string += 'x' if mode & stat.S_IXGRP else '-'
        permission_string += 'r' if mode & stat.S_IROTH else '-'
        permission_string += 'w' if mode & stat.S_IWOTH else '-'
        permission_string += 'x' if mode & stat.S_IXOTH else '-'

        return {
            'mode': mode,
            'readable': os.access(file_path, os.R_OK),
            'writable': os.access(file_path, os.W_OK),
            'executable': os.access(file_path, os.X_OK),
            'permission_string': permission_string
        }
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied accessing file: {file_path}")