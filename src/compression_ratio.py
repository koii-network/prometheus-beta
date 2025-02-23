import os

def calculate_compression_ratio(original_file_path, compressed_file_path):
    """
    Calculate the compression ratio of a file.
    
    Compression Ratio = Original File Size / Compressed File Size
    
    Args:
        original_file_path (str): Path to the original file
        compressed_file_path (str): Path to the compressed file
    
    Returns:
        float: Compression ratio (always >= 1)
        
    Raises:
        FileNotFoundError: If either file does not exist
        ValueError: If file sizes are invalid or compressed file is larger than original
    """
    # Validate file existence
    if not os.path.exists(original_file_path):
        raise FileNotFoundError(f"Original file not found: {original_file_path}")
    
    if not os.path.exists(compressed_file_path):
        raise FileNotFoundError(f"Compressed file not found: {compressed_file_path}")
    
    # Get file sizes
    original_size = os.path.getsize(original_file_path)
    compressed_size = os.path.getsize(compressed_file_path)
    
    # Validate file sizes
    if original_size <= 0:
        raise ValueError("Original file size must be greater than 0")
    
    if compressed_size <= 0:
        raise ValueError("Compressed file size must be greater than 0")
    
    if compressed_size > original_size:
        raise ValueError("Compressed file size cannot be larger than original file size")
    
    # Calculate and return compression ratio
    compression_ratio = original_size / compressed_size
    return round(compression_ratio, 2)