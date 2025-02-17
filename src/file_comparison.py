import filecmp
import os

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
    """
    # Check if files exist
    if not os.path.exists(file1_path):
        raise FileNotFoundError(f"File {file1_path} does not exist")
    if not os.path.exists(file2_path):
        raise FileNotFoundError(f"File {file2_path} does not exist")
    
    # Check file sizes first for quick comparison
    if os.path.getsize(file1_path) != os.path.getsize(file2_path):
        return False
    
    # Use filecmp for detailed comparison
    return filecmp.cmp(file1_path, file2_path, shallow=False)