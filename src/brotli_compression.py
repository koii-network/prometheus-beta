import brotli

def compress_data(data, quality=11):
    """
    Compress data using Brotli compression algorithm.
    
    Args:
        data (bytes): The input data to compress.
        quality (int, optional): Compression level (0-11). 
                                 Defaults to 11 (highest compression).
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If quality is not between 0 and 11.
    """
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    # Validate compression quality
    if not 0 <= quality <= 11:
        raise ValueError("Compression quality must be between 0 and 11")
    
    # Compress the data using Brotli
    return brotli.compress(data, quality=quality)

def decompress_data(compressed_data):
    """
    Decompress Brotli compressed data.
    
    Args:
        compressed_data (bytes): The Brotli compressed data.
    
    Returns:
        bytes: Decompressed original data.
    
    Raises:
        TypeError: If input is not bytes.
        brotli.Error: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress the data using Brotli
    return brotli.decompress(compressed_data)