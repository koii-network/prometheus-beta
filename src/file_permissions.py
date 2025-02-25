import os
import stat

def get_file_permissions(file_path):
    """
    Retrieve the file permissions for a given file.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict: A dictionary containing file permission details:
            - 'numeric': Numeric representation of file permissions (e.g., 644)
            - 'readable': Readable permission string (e.g., 'rw-r--r--')
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
        FileNotFoundError: If the file does not exist
        PermissionError: If the file cannot be accessed
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Get file status
        file_stat = os.stat(file_path)
        mode = file_stat.st_mode
        
        # Convert mode to numeric representation
        numeric_permissions = stat.S_IMODE(mode)
        
        # Create readable permission string
        readable_permissions = ''
        for who, mask in [
            (stat.S_IRUSR, stat.S_IWUSR, stat.S_IXUSR),  # owner
            (stat.S_IRGRP, stat.S_IWGRP, stat.S_IXGRP),  # group
            (stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH)   # others
        ]:
            readable_permissions += 'r' if mode & who else '-'
            readable_permissions += 'w' if mode & mask[1] else '-'
            readable_permissions += 'x' if mode & mask[2] else '-'
        
        return {
            'numeric': numeric_permissions,
            'readable': readable_permissions,
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
        raise
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing file: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error retrieving file permissions: {str(e)}")