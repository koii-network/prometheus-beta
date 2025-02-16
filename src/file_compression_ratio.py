import os
import zlib

def calculate_compression_ratio(file_path):
    """
    Calculate the compression ratio of a file using zlib compression.
    
    Args:
        file_path (str): Path to the file to analyze
    
    Returns:
        float: Compression ratio (original_size / compressed_size)
        
    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the file is empty or cannot be read
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check file size
    original_size = os.path.getsize(file_path)
    if original_size == 0:
        raise ValueError("Cannot calculate compression ratio for an empty file")
    
    # Read file content
    try:
        with open(file_path, 'rb') as f:
            file_content = f.read()
    except Exception as e:
        raise ValueError(f"Error reading file: {e}")
    
    # Compress content
    compressed_content = zlib.compress(file_content)
    compressed_size = len(compressed_content)
    
    # Avoid division by zero
    if compressed_size == 0:
        return 1.0
    
    # Calculate and return compression ratio
    return original_size / compressed_size