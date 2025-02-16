import lzo
import struct

def lzo_compress(data):
    """
    Compress data using LZO compression algorithm.
    
    Args:
        data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If compression fails
    """
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    # If input is empty, return empty bytes
    if not data:
        return b''
    
    try:
        # Compress the data
        compressed = lzo.compress(data)
        return compressed
    except Exception as e:
        raise ValueError(f"Compression failed: {str(e)}")

def lzo_decompress(compressed_data):
    """
    Decompress data using LZO compression algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # If input is empty, return empty bytes
    if not compressed_data:
        return b''
    
    try:
        # Decompress the data
        decompressed = lzo.decompress(compressed_data)
        return decompressed
    except Exception as e:
        raise ValueError(f"Decompression failed: {str(e)}")