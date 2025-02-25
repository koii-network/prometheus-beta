import os
import hashlib

def are_files_identical(file1_path: str, file2_path: str) -> bool:
    """
    Compare two files to check if they are identical.
    
    Args:
        file1_path (str): Path to the first file
        file2_path (str): Path to the second file
    
    Returns:
        bool: True if files are identical, False otherwise
    
    Raises:
        FileNotFoundError: If either of the files does not exist
        IOError: If there's an issue reading the files
    """
    # Check if files exist
    if not os.path.exists(file1_path):
        raise FileNotFoundError(f"First file not found: {file1_path}")
    if not os.path.exists(file2_path):
        raise FileNotFoundError(f"Second file not found: {file2_path}")
    
    # Check file sizes first for quick comparison
    if os.path.getsize(file1_path) != os.path.getsize(file2_path):
        return False
    
    # Compare file contents using hash
    def calculate_file_hash(filepath):
        """Calculate SHA-256 hash of a file."""
        hash_sha256 = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    
    try:
        return calculate_file_hash(file1_path) == calculate_file_hash(file2_path)
    except IOError as e:
        raise IOError(f"Error reading file: {e}")