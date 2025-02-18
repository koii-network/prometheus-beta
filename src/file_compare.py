import os
import hashlib

def are_files_identical(file1_path: str, file2_path: str) -> bool:
    """
    Compare two files and check if they are identical.
    
    Args:
        file1_path (str): Path to the first file
        file2_path (str): Path to the second file
    
    Returns:
        bool: True if files are identical, False otherwise
    
    Raises:
        FileNotFoundError: If either file does not exist
        IsADirectoryError: If either path is a directory
    """
    # Check if both files exist
    if not os.path.exists(file1_path):
        raise FileNotFoundError(f"File not found: {file1_path}")
    if not os.path.exists(file2_path):
        raise FileNotFoundError(f"File not found: {file2_path}")
    
    # Check if both are files (not directories)
    if os.path.isdir(file1_path):
        raise IsADirectoryError(f"Path is a directory: {file1_path}")
    if os.path.isdir(file2_path):
        raise IsADirectoryError(f"Path is a directory: {file2_path}")
    
    # Check file sizes first (quick comparison)
    if os.path.getsize(file1_path) != os.path.getsize(file2_path):
        return False
    
    # Compute and compare file hashes for precise comparison
    def file_hash(filepath):
        hasher = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    return file_hash(file1_path) == file_hash(file2_path)