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
    
    try:
        # Compress the data using LZO algorithm
        compressed_data = lzo.compress(data)
        
        # Prepend original data length to allow for decompression
        original_length = len(data)
        return struct.pack('!I', original_length) + compressed_data
    
    except Exception as e:
        raise ValueError(f"LZO compression failed: {str(e)}")

def lzo_decompress(compressed_data):
    """
    Decompress data compressed with LZO algorithm.
    
    Args:
        compressed_data (bytes): Compressed data with prepended original length
    
    Returns:
        bytes: Decompressed original data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    try:
        # Extract original data length
        original_length = struct.unpack('!I', compressed_data[:4])[0]
        
        # Decompress the data
        decompressed_data = lzo.decompress(compressed_data[4:], original_length)
        
        return decompressed_data
    
    except Exception as e:
        raise ValueError(f"LZO decompression failed: {str(e)}")