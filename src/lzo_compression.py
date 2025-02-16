import lzo
import struct

def lzo_compress(data):
    """
    Compress data using Lempel-Ziv-Oberhumer (LZO) compression algorithm.
    
    Args:
        data (bytes or str): The input data to compress.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input data is empty.
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert string to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Ensure input is bytes
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    try:
        # Compress the data using LZO
        compressed_data = lzo.compress(data)
        
        # Prepend original data length for decompression
        original_length = len(data)
        compressed_with_length = struct.pack('>I', original_length) + compressed_data
        
        return compressed_with_length
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def lzo_decompress(compressed_data):
    """
    Decompress data compressed with LZO algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input data is too short or invalid.
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if len(compressed_data) < 4:
        raise ValueError("Compressed data is too short")
    
    try:
        # Extract original length
        original_length = struct.unpack('>I', compressed_data[:4])[0]
        
        # Decompress the data
        decompressed_data = lzo.decompress(compressed_data[4:], original_length)
        
        return decompressed_data
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")