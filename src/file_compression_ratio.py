import os
import zlib

def calculate_compression_ratio(file_path):
    """
    Calculate the compression ratio of a file.
    
    Args:
        file_path (str): Path to the file to analyze
    
    Returns:
        float: Compression ratio (compressed_size / original_size)
        
    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the file is empty
    """
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check file size
    original_size = os.path.getsize(file_path)
    if original_size == 0:
        raise ValueError("Cannot calculate compression ratio for an empty file")
    
    # Read file contents
    with open(file_path, 'rb') as f:
        file_contents = f.read()
    
    # Compress file contents using zlib
    compressed_contents = zlib.compress(file_contents)
    compressed_size = len(compressed_contents)
    
    # Calculate and return compression ratio
    return compressed_size / original_size