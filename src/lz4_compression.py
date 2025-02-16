import lz4.frame

def compress_lz4(data: bytes) -> bytes:
    """
    Compress input bytes using LZ4 compression algorithm.
    
    Args:
        data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty
    """
    # Validate input
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Compress the data using LZ4 frame compression
    return lz4.frame.compress(data)

def decompress_lz4(compressed_data: bytes) -> bytes:
    """
    Decompress LZ4 compressed bytes.
    
    Args:
        compressed_data (bytes): Compressed data to be decompressed
    
    Returns:
        bytes: Decompressed original data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty
    """
    # Validate input
    if not isinstance(data := compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Decompress the data using LZ4 frame decompression
    return lz4.frame.decompress(compressed_data)