import os
import shutil
from typing import Union, Optional

def backup_file(file_path: str, backup_dir: Optional[str] = None) -> str:
    """
    Create a backup of a given file.

    Args:
        file_path (str): Path to the file to be backed up
        backup_dir (Optional[str], optional): Directory to store the backup. 
                                             Defaults to creating a backup in the same directory.

    Returns:
        str: Path to the created backup file

    Raises:
        FileNotFoundError: If the source file does not exist
        ValueError: If the source path is not a file
        PermissionError: If there are insufficient permissions to read/write
    """
    # Validate input file exists and is a file
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Source file not found: {file_path}")
    
    if not os.path.isfile(file_path):
        raise ValueError(f"Source path is not a file: {file_path}")
    
    # Determine backup directory
    if backup_dir is None:
        # Default to same directory as source file
        backup_dir = os.path.dirname(file_path) or '.'
    
    # Ensure backup directory exists
    os.makedirs(backup_dir, exist_ok=True)
    
    # Generate backup filename
    original_filename = os.path.basename(file_path)
    timestamp = os.getpid()  # Using PID as a simple unique identifier
    backup_filename = f"{original_filename}.backup.{timestamp}"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    # Perform file copy
    try:
        shutil.copy2(file_path, backup_path)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to backup file: {file_path}")
    
    return backup_path