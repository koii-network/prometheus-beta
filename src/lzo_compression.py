import lzo
import struct

def compress_lzo(data):
    """
    Compress data using LZO compression algorithm.
    
    Args:
        data (bytes): The input data to be compressed.
    
    Returns:
        bytes: Compressed data with a header containing the original data length.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input data is empty.
    """
    # Validate input
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Compress the data
    compressed = lzo.compress(data)
    
    # Prepend the original data length to the compressed data
    # This allows for potential decompression later
    original_length = len(data)
    header = struct.pack('!I', original_length)
    
    return header + compressed

def decompress_lzo(compressed_data):
    """
    Decompress LZO compressed data.
    
    Args:
        compressed_data (bytes): The compressed data with original length header.
    
    Returns:
        bytes: Decompressed original data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input data is too short or invalid.
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if len(compressed_data) < 4:
        raise ValueError("Compressed data is too short")
    
    # Extract original length from header
    original_length = struct.unpack('!I', compressed_data[:4])[0]
    
    # Decompress the data (excluding the header)
    decompressed = lzo.decompress(compressed_data[4:])
    
    # Verify decompressed data length
    if len(decompressed) != original_length:
        raise ValueError("Decompression failed: length mismatch")
    
    return decompressed