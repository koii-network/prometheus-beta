import os
import shutil
from datetime import datetime

def create_file_backup(file_path, backup_dir=None):
    """
    Create a backup of a given file.
    
    Args:
        file_path (str): Path to the file to be backed up
        backup_dir (str, optional): Directory to store the backup. 
                                    If None, backup in the same directory as the original file.
    
    Returns:
        str: Path to the created backup file
    
    Raises:
        FileNotFoundError: If the source file does not exist
        PermissionError: If there are permission issues
        IsADirectoryError: If file_path is a directory
    """
    # Validate input file exists and is a file
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Source file not found: {file_path}")
    
    if not os.path.isfile(file_path):
        raise IsADirectoryError(f"Path is not a file: {file_path}")
    
    # Determine backup directory
    if backup_dir is None:
        backup_dir = os.path.dirname(file_path)
    
    # Ensure backup directory exists
    os.makedirs(backup_dir, exist_ok=True)
    
    # Generate backup filename with timestamp
    base_filename = os.path.basename(file_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{base_filename}.{timestamp}.bak"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    # Copy the file
    try:
        shutil.copy2(file_path, backup_path)
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to backup {file_path}")
    
    return backup_path