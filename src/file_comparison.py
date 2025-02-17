import os
import hashlib

def are_files_identical(file1_path, file2_path):
    """
    Compare two files to check if they are identical.
    
    Args:
        file1_path (str): Path to the first file
        file2_path (str): Path to the second file
    
    Returns:
        bool: True if files are identical, False otherwise
    
    Raises:
        FileNotFoundError: If either file does not exist
        IOError: If there's an issue reading the files
    """
    # Check if files exist
    if not os.path.exists(file1_path):
        raise FileNotFoundError(f"File {file1_path} does not exist")
    if not os.path.exists(file2_path):
        raise FileNotFoundError(f"File {file2_path} does not exist")
    
    # Compare file sizes first for quick elimination
    if os.path.getsize(file1_path) != os.path.getsize(file2_path):
        return False
    
    # Calculate file hash to compare contents
    def calculate_file_hash(file_path):
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    # Compare file hashes
    return calculate_file_hash(file1_path) == calculate_file_hash(file2_path)