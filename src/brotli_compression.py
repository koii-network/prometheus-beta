import brotli

def compress_brotli(data: str, quality: int = 11) -> bytes:
    """
    Compress input data using Brotli compression algorithm.
    
    Args:
        data (str): The input string to compress
        quality (int, optional): Compression quality (0-11). Defaults to 11 (highest compression).
    
    Returns:
        bytes: Compressed data in Brotli format
    
    Raises:
        ValueError: If quality is not between 0 and 11
        TypeError: If input is not a string
    """
    # Validate input type
    if not isinstance(data, str):
        raise TypeError("Input must be a string")
    
    # Validate compression quality
    if quality < 0 or quality > 11:
        raise ValueError("Compression quality must be between 0 and 11")
    
    # Convert string to bytes and compress
    encoded_data = data.encode('utf-8')
    compressed_data = brotli.compress(encoded_data, quality)
    
    return compressed_data

def decompress_brotli(compressed_data: bytes) -> str:
    """
    Decompress Brotli compressed data back to original string.
    
    Args:
        compressed_data (bytes): Brotli compressed data
    
    Returns:
        str: Decompressed original string
    
    Raises:
        TypeError: If input is not bytes
        brotli.error: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress and convert back to string
    decompressed_data = brotli.decompress(compressed_data)
    return decompressed_data.decode('utf-8')