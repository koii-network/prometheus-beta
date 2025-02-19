import lzo
import struct

def compress_lzop(input_data):
    """
    Compress data using LZOP compression algorithm.
    
    Args:
        input_data (bytes): The data to be compressed.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input data is empty.
    """
    # Input validation
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    try:
        # Compress the data using python-lzo library
        compressed_data = lzo.compress(input_data)
        
        # Optionally, you can add a header with original size for decompression
        header = struct.pack('>I', len(input_data))
        return header + compressed_data
    
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")