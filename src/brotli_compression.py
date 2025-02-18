import brotli

def compress_data(data: bytes, quality: int = 11) -> bytes:
    """
    Compress input data using Brotli compression algorithm.
    
    Args:
        data (bytes): The input data to compress
        quality (int, optional): Compression quality (0-11). Defaults to 11 (highest compression).
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If quality is outside valid range
    """
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    # Validate compression quality
    if quality < 0 or quality > 11:
        raise ValueError("Compression quality must be between 0 and 11")
    
    # Compress the data
    return brotli.compress(data, quality)

def decompress_data(compressed_data: bytes) -> bytes:
    """
    Decompress Brotli compressed data.
    
    Args:
        compressed_data (bytes): The Brotli compressed data to decompress
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        brotli.error: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress the data
    return brotli.decompress(compressed_data)