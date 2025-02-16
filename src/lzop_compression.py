import lzo
import os

def lzop_compress(input_data):
    """
    Compress data using the LZOP compression algorithm.
    
    Args:
        input_data (bytes): The input data to be compressed.
    
    Returns:
        bytes: The compressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input data is empty.
    """
    # Validate input
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    try:
        # Compress the data using LZO
        compressed_data = lzo.compress(input_data)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def lzop_decompress(compressed_data):
    """
    Decompress data that was compressed using the LZOP compression algorithm.
    
    Args:
        compressed_data (bytes): The compressed data to be decompressed.
    
    Returns:
        bytes: The decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input data is empty.
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    try:
        # Decompress the data using LZO
        decompressed_data = lzo.decompress(compressed_data)
        return decompressed_data
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")