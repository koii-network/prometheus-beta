import zlib

def deflate_compress(data: str | bytes, compression_level: int = 6) -> bytes:
    """
    Compress input data using Deflate compression algorithm.
    
    Args:
        data (str | bytes): The input data to compress. 
                             If str, it will be encoded to UTF-8 bytes.
        compression_level (int, optional): Compression level from 0-9. 
                                           Defaults to 6 (default zlib compression).
    
    Returns:
        bytes: Compressed data using Deflate algorithm.
    
    Raises:
        TypeError: If input is not str or bytes.
        ValueError: If compression level is not between 0 and 9.
    """
    # Validate compression level
    if compression_level < 0 or compression_level > 9:
        raise ValueError("Compression level must be between 0 and 9")
    
    # Convert str to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be str or bytes")
    
    # Compress using zlib (which implements Deflate)
    compressed_data = zlib.compress(data, compression_level)
    
    return compressed_data

def deflate_decompress(compressed_data: bytes) -> bytes:
    """
    Decompress data that was compressed using Deflate algorithm.
    
    Args:
        compressed_data (bytes): The compressed data to decompress.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        zlib.error: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress using zlib (which implements Deflate)
    decompressed_data = zlib.decompress(compressed_data)
    
    return decompressed_data