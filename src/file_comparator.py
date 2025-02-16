import os
import filecmp

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
    # Check if files exist
    if not os.path.exists(file1_path):
        raise FileNotFoundError(f"First file not found: {file1_path}")
    if not os.path.exists(file2_path):
        raise FileNotFoundError(f"Second file not found: {file2_path}")
    
    # Check if paths are files, not directories
    if os.path.isdir(file1_path):
        raise IsADirectoryError(f"First path is a directory: {file1_path}")
    if os.path.isdir(file2_path):
        raise IsADirectoryError(f"Second path is a directory: {file2_path}")
    
    # Use filecmp to compare files
    return filecmp.cmp(file1_path, file2_path, shallow=False)