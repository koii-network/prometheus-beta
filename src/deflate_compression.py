import zlib

def deflate_compress(data: str, compression_level: int = 6) -> bytes:
    """
    Compress input data using the Deflate compression algorithm.
    
    Args:
        data (str): The input string to be compressed.
        compression_level (int, optional): Compression level from 0-9. 
                                           Defaults to 6 (default zlib compression).
    
    Returns:
        bytes: Compressed data using Deflate algorithm.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If compression level is not between 0 and 9.
    """
    # Validate input types
    if not isinstance(data, str):
        raise TypeError("Input must be a string")
    
    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")
    
    # Convert string to bytes and compress using zlib (Deflate implementation)
    compressed_data = zlib.compress(data.encode('utf-8'), compression_level)
    
    return compressed_data

def deflate_decompress(compressed_data: bytes) -> str:
    """
    Decompress data compressed with the Deflate algorithm.
    
    Args:
        compressed_data (bytes): The compressed data to decompress.
    
    Returns:
        str: Decompressed string.
    
    Raises:
        TypeError: If input is not bytes.
        zlib.error: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress using zlib (Deflate implementation)
    decompressed_data = zlib.decompress(compressed_data).decode('utf-8')
    
    return decompressed_data