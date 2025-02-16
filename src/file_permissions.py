import os
import stat

def get_file_permissions(file_path):
    """
    Get the file permissions of a given file.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        dict: A dictionary containing file permission details.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there's no permission to access the file.
    """
    try:
        file_stat = os.stat(file_path)
        mode = file_stat.st_mode
        
        return {
            'raw_mode': mode,
            'owner_read': bool(mode & stat.S_IRUSR),
            'owner_write': bool(mode & stat.S_IWUSR),
            'owner_execute': bool(mode & stat.S_IXUSR),
            'group_read': bool(mode & stat.S_IRGRP),
            'group_write': bool(mode & stat.S_IWGRP),
            'group_execute': bool(mode & stat.S_IXGRP),
            'others_read': bool(mode & stat.S_IROTH),
            'others_write': bool(mode & stat.S_IWOTH),
            'others_execute': bool(mode & stat.S_IXOTH),
            'is_directory': stat.S_ISDIR(mode),
            'is_file': stat.S_ISREG(mode),
            'is_symlink': stat.S_ISLNK(mode)
        }
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing {file_path}.")