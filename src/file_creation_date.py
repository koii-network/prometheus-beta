import os
import platform

def get_file_creation_date(file_path):
    """
    Get the creation date of a file across different platforms.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        float: Timestamp of file creation.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If file creation time cannot be retrieved.
    """
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Platform-specific file creation time retrieval
    try:
        # Windows
        if platform.system() == 'Windows':
            return os.path.getctime(file_path)
        
        # macOS
        if platform.system() == 'Darwin':
            import stat
            return os.stat(file_path).st_birthtime
        
        # Linux and other Unix-like systems
        # Note: Not all Linux filesystems support creation time
        stat_info = os.stat(file_path)
        return stat_info.st_ctime
    
    except Exception as e:
        raise OSError(f"Could not retrieve file creation time: {str(e)}")