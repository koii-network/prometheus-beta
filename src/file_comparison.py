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
        IOError: If there's an error reading the files
    """
    # Check if files exist
    if not os.path.exists(file1_path):
        raise FileNotFoundError(f"File not found: {file1_path}")
    if not os.path.exists(file2_path):
        raise FileNotFoundError(f"File not found: {file2_path}")
    
    # Check file sizes first for quick comparison
    if os.path.getsize(file1_path) != os.path.getsize(file2_path):
        return False
    
    # Calculate and compare file hashes
    def file_hash(filename):
        hasher = hashlib.sha256()
        with open(filename, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    return file_hash(file1_path) == file_hash(file2_path)