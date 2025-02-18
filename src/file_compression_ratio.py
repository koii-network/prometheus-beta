import os
import zlib

def calculate_compression_ratio(file_path):
    """
    Calculate the compression ratio of a file.
    
    Args:
        file_path (str): Path to the file to analyze.
    
    Returns:
        float: Compression ratio (original_size / compressed_size). 
               Returns 1.0 if compression doesn't reduce file size.
               Returns None if file cannot be read or is empty.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there are permission issues reading the file.
    """
    # Validate file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check file size
    original_size = os.path.getsize(file_path)
    
    # Handle empty file case
    if original_size == 0:
        return None
    
    # Read file content
    try:
        with open(file_path, 'rb') as f:
            file_content = f.read()
    except (PermissionError, IOError) as e:
        raise PermissionError(f"Cannot read file: {file_path}. Error: {e}")
    
    # Compress file content using zlib
    compressed_content = zlib.compress(file_content)
    compressed_size = len(compressed_content)
    
    # Calculate compression ratio (original_size / compressed_size)
    # If compression increases size, return 1.0
    return max(1.0, original_size / compressed_size)