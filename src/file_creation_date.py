import os
import platform
import datetime

def get_file_creation_date(file_path):
    """
    Get the creation date of a file across different operating systems.
    
    Args:
        file_path (str): Path to the file
    
    Returns:
        datetime.datetime: The creation date of the file
    
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If there's no permission to access the file
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Platform-specific file creation time retrieval
    try:
        # Windows
        if platform.system() == 'Windows':
            return datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        
        # macOS
        elif platform.system() == 'Darwin':
            stat = os.stat(file_path)
            try:
                # Try to get creation time on macOS
                return datetime.datetime.fromtimestamp(stat.st_birthtime)
            except AttributeError:
                # Fallback to modification time if creation time not available
                return datetime.datetime.fromtimestamp(stat.st_mtime)
        
        # Linux and other Unix-like systems
        else:
            stat = os.stat(file_path)
            # On most Unix systems, try to use metadata change time
            return datetime.datetime.fromtimestamp(stat.st_ctime)
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing file: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error retrieving file creation date: {str(e)}")