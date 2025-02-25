import os
import filecmp

def are_files_identical(file1_path: str, file2_path: str) -> bool:
    """
    Compare two files and check if they are identical.

    Args:
        file1_path (str): Path to the first file
        file2_path (str): Path to the second file

    Returns:
        bool: True if files are identical, False otherwise

    Raises:
        FileNotFoundError: If either of the files does not exist
        TypeError: If input paths are not strings
        PermissionError: If there are permission issues reading the files
    """
    # Validate input types
    if not isinstance(file1_path, str) or not isinstance(file2_path, str):
        raise TypeError("File paths must be strings")

    # Check if files exist
    if not os.path.exists(file1_path):
        raise FileNotFoundError(f"File not found: {file1_path}")
    if not os.path.exists(file2_path):
        raise FileNotFoundError(f"File not found: {file2_path}")

    # Check if both paths point to files (not directories)
    if not os.path.isfile(file1_path) or not os.path.isfile(file2_path):
        return False

    # Compare file sizes first for quick elimination
    if os.path.getsize(file1_path) != os.path.getsize(file2_path):
        return False

    # Use filecmp for comprehensive file comparison
    return filecmp.cmp(file1_path, file2_path, shallow=False)