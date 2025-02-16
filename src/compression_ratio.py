import os
import zlib

def calculate_compression_ratio(file_path):
    """
    Calculate the compression ratio of a file.
    
    Args:
        file_path (str): Path to the file to analyze
    
    Returns:
        float: Compression ratio (original_size / compressed_size)
               Returns 1.0 if compression is not possible or file is empty
    
    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If there are permission issues reading the file
    """
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Get original file size
    original_size = os.path.getsize(file_path)
    
    # Handle empty file case
    if original_size == 0:
        return 1.0
    
    # Read file contents
    try:
        with open(file_path, 'rb') as f:
            file_contents = f.read()
    except PermissionError:
        raise PermissionError(f"Permission denied reading file: {file_path}")
    
    # Compress file contents using zlib
    compressed_contents = zlib.compress(file_contents)
    compressed_size = len(compressed_contents)
    
    # Calculate and return compression ratio
    # If compression increases file size, return 1.0
    return max(1.0, original_size / compressed_size)