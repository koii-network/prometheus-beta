import brotli

def compress_brotli(data, compression_level=11):
    """
    Compress data using Brotli compression algorithm.
    
    Args:
        data (bytes or str): The data to compress. If str, it will be encoded to bytes.
        compression_level (int, optional): Compression level from 0-11. Defaults to 11 (highest compression).
    
    Returns:
        bytes: Compressed data using Brotli algorithm.
    
    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If compression level is out of range.
    """
    # Validate input type
    if not isinstance(data, (bytes, str)):
        raise TypeError("Input must be bytes or str")
    
    # Convert str to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate compression level
    if not 0 <= compression_level <= 11:
        raise ValueError("Compression level must be between 0 and 11")
    
    # Compress using Brotli
    return brotli.compress(data, quality=compression_level)

def decompress_brotli(compressed_data):
    """
    Decompress Brotli compressed data.
    
    Args:
        compressed_data (bytes): Brotli compressed data.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        brotli.error: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress using Brotli
    return brotli.decompress(compressed_data)