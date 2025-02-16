import lzo
import struct

def lzop_compress(data):
    """
    Compress data using LZOP compression algorithm.
    
    Args:
        data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input data is empty
    """
    # Validate input
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    try:
        # Compress the data using python-lzo library
        compressed = lzo.compress(data)
        
        # Prepend original data length to the compressed data
        # This helps in potential decompression later
        original_length = len(data)
        compressed_length = len(compressed)
        
        # Pack the original length as a 4-byte integer
        header = struct.pack('>I', original_length)
        
        return header + compressed
    
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")