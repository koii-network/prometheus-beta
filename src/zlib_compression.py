import zlib

def compress_data(data, compression_level=6):
    """
    Compress input data using Zlib compression algorithm.
    
    Args:
        data (bytes or str): The data to compress. 
                              If str, it will be encoded to bytes first.
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
    
    # Compress data using zlib
    return zlib.compress(data, compression_level)

def decompress_data(compressed_data):
    """
    Decompress Zlib compressed data.
    
    Args:
        compressed_data (bytes): The data to decompress
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        zlib.error: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress data using zlib
    return zlib.decompress(compressed_data)