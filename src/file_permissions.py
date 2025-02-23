import os
import stat

def get_file_permissions(file_path):
    """
    Retrieve the file permissions of a given file.

    Args:
        file_path (str): Path to the file whose permissions are to be retrieved.

    Returns:
        dict: A dictionary containing file permission details:
            - 'numeric': Octal representation of file permissions (e.g., '0o755')
            - 'readable': Human-readable permission string (e.g., 'rwxr-xr-x')
            - 'owner_read': Boolean indicating if owner can read
            - 'owner_write': Boolean indicating if owner can write
            - 'owner_execute': Boolean indicating if owner can execute
            - 'group_read': Boolean indicating if group can read
            - 'group_write': Boolean indicating if group can write
            - 'group_execute': Boolean indicating if group can execute
            - 'others_read': Boolean indicating if others can read
            - 'others_write': Boolean indicating if others can write
            - 'others_execute': Boolean indicating if others can execute

    Raises:
        FileNotFoundError: If the specified file does not exist
        PermissionError: If the file cannot be accessed
        TypeError: If the file_path is not a string
    """
    # Validate input
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")

    try:
        # Get file stats
        file_stat = os.stat(file_path)
        mode = file_stat.st_mode

        # Calculate permissions
        return {
            'numeric': oct(mode & 0o777),
            'readable': stat.filemode(mode)[1:],
            'owner_read': bool(mode & stat.S_IRUSR),
            'owner_write': bool(mode & stat.S_IWUSR),
            'owner_execute': bool(mode & stat.S_IXUSR),
            'group_read': bool(mode & stat.S_IRGRP),
            'group_write': bool(mode & stat.S_IWGRP),
            'group_execute': bool(mode & stat.S_IXGRP),
            'others_read': bool(mode & stat.S_IROTH),
            'others_write': bool(mode & stat.S_IWOTH),
            'others_execute': bool(mode & stat.S_IXOTH)
        }
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing: {file_path}")