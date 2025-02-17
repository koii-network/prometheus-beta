import os
import stat

def get_file_permissions(file_path):
    """
    Get the file permissions of a given file path.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        dict: A dictionary containing file permission details
        - 'octal': Octal representation of permissions (e.g., '0o644')
        - 'readable': Human-readable permission string (e.g., 'rw-r--r--')
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
        PermissionError: If the file is not accessible
    """
    try:
        file_stat = os.stat(file_path)
        mode = file_stat.st_mode
        
        # Octal representation
        octal_perm = oct(mode & 0o777)
        
        # Readable permission string
        readable_perm = stat.filemode(mode)
        
        return {
            'octal': octal_perm,
            'readable': readable_perm,
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
        raise PermissionError(f"Permission denied accessing file: {file_path}")