import zlib

def compress_data(data, compression_level=6):
    """
    Compress input data using Zlib compression.
    
    Args:
        data (bytes or str): Data to be compressed
        compression_level (int, optional): Compression level from 0-9. Defaults to 6.
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If compression level is out of range
    """
    if not isinstance(data, (bytes, str)):
        raise TypeError("Input must be bytes or str")
    
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")
    
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    return zlib.compress(data, compression_level)

def decompress_data(compressed_data):
    """
    Decompress data previously compressed with Zlib.
    
    Args:
        compressed_data (bytes): Compressed data to decompress
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        zlib.error: If data is not valid compressed data
    """
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    return zlib.decompress(compressed_data)