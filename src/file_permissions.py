import os
import stat

def get_file_permissions(file_path):
    """
    Get the file permissions of a given file.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        dict: A dictionary containing file permission details
            - 'numeric': Numeric representation of permissions (e.g., 644)
            - 'readable': Human-readable permission string (e.g., 'rw-r--r--')
            - 'owner_can_read': Boolean indicating if owner can read
            - 'owner_can_write': Boolean indicating if owner can write
            - 'owner_can_execute': Boolean indicating if owner can execute
            - 'group_can_read': Boolean indicating if group can read
            - 'group_can_write': Boolean indicating if group can write
            - 'group_can_execute': Boolean indicating if group can execute
            - 'others_can_read': Boolean indicating if others can read
            - 'others_can_write': Boolean indicating if others can write
            - 'others_can_execute': Boolean indicating if others can execute
    
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If there's no permission to access the file
    """
    try:
        # Get file stat
        file_stat = os.stat(file_path)
        mode = file_stat.st_mode
        
        # Convert mode to numeric permission
        numeric_perm = stat.S_IMODE(mode)
        numeric_str = f"{numeric_perm:03o}"
        
        # Readable permission string
        readable_perm = ''
        readable_perm += 'r' if mode & stat.S_IRUSR else '-'
        readable_perm += 'w' if mode & stat.S_IWUSR else '-'
        readable_perm += 'x' if mode & stat.S_IXUSR else '-'
        readable_perm += 'r' if mode & stat.S_IRGRP else '-'
        readable_perm += 'w' if mode & stat.S_IWGRP else '-'
        readable_perm += 'x' if mode & stat.S_IXGRP else '-'
        readable_perm += 'r' if mode & stat.S_IROTH else '-'
        readable_perm += 'w' if mode & stat.S_IWOTH else '-'
        readable_perm += 'x' if mode & stat.S_IXOTH else '-'
        
        return {
            'numeric': numeric_str,
            'readable': readable_perm,
            'owner_can_read': bool(mode & stat.S_IRUSR),
            'owner_can_write': bool(mode & stat.S_IWUSR),
            'owner_can_execute': bool(mode & stat.S_IXUSR),
            'group_can_read': bool(mode & stat.S_IRGRP),
            'group_can_write': bool(mode & stat.S_IWGRP),
            'group_can_execute': bool(mode & stat.S_IXGRP),
            'others_can_read': bool(mode & stat.S_IROTH),
            'others_can_write': bool(mode & stat.S_IWOTH),
            'others_can_execute': bool(mode & stat.S_IXOTH)
        }
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing file: {file_path}")