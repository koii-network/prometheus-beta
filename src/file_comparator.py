import os
import hashlib

def are_files_identical(file1_path, file2_path):
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
    # Check if files exist and are not directories
    if not os.path.isfile(file1_path):
        raise FileNotFoundError(f"File not found: {file1_path}")
    if not os.path.isfile(file2_path):
        raise FileNotFoundError(f"File not found: {file2_path}")
    
    # Check file size first (quick comparison)
    if os.path.getsize(file1_path) != os.path.getsize(file2_path):
        return False
    
    # Compute hash of both files
    def file_hash(filepath):
        hasher = hashlib.md5()
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    return file_hash(file1_path) == file_hash(file2_path)