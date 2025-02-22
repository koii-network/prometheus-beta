import os
import shutil
from datetime import datetime

def create_file_backup(file_path, backup_dir=None):
    """
    Create a backup of a given file.
    
    Args:
        file_path (str): Path to the file to be backed up
        backup_dir (str, optional): Directory to store backups. 
                                    If None, creates a backup in the same directory.
    
    Returns:
        str: Path to the created backup file
    
    Raises:
        FileNotFoundError: If the source file does not exist
        PermissionError: If there are permission issues
        ValueError: If file_path is invalid
    """
    # Validate input
    if not file_path or not isinstance(file_path, str):
        raise ValueError("Invalid file path")
    
    # Normalize the path
    file_path = os.path.abspath(file_path)
    
    # Check if source file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Source file not found: {file_path}")
    
    # Determine backup directory
    if backup_dir is None:
        backup_dir = os.path.dirname(file_path)
    else:
        # Ensure backup directory exists
        os.makedirs(backup_dir, exist_ok=True)
    
    # Generate backup filename with timestamp
    filename = os.path.basename(file_path)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{filename}.{timestamp}.bak"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    # Create backup
    try:
        shutil.copy2(file_path, backup_path)
        return backup_path
    except PermissionError:
        raise PermissionError(f"Permission denied when creating backup: {backup_path}")