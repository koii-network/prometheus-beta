import zlib

def deflate_compress(data, compression_level=6):
    """
    Compress data using the Deflate compression algorithm.
    
    Args:
        data (bytes or str): The input data to compress. 
                              If str is provided, it will be encoded to bytes.
        compression_level (int, optional): Compression level from 0-9. 
                                           Defaults to 6 (default zlib compression).
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If compression level is not between 0 and 9
    """
    # Validate input type
    if not isinstance(data, (bytes, str)):
        raise TypeError("Input must be bytes or str")
    
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")
    
    # Compress using zlib (which implements Deflate)
    compressed_data = zlib.compress(data, compression_level)
    
    return compressed_data

def deflate_decompress(compressed_data):
    """
    Decompress data that was compressed using the Deflate algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        zlib.error: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress using zlib (which implements Deflate)
    decompressed_data = zlib.decompress(compressed_data)
    
    return decompressed_data