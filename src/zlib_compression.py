import zlib

def compress_data(data, compression_level=6):
    """
    Compress input data using Zlib compression algorithm.
    
    Args:
        data (bytes or str): The data to be compressed. 
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
    
    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")
    
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Compress the data
    compressed_data = zlib.compress(data, compression_level)
    
    return compressed_data

def decompress_data(compressed_data):
    """
    Decompress Zlib compressed data.
    
    Args:
        compressed_data (bytes): The compressed data to decompress
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        zlib.error: If data is not valid compressed data
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress the data
    decompressed_data = zlib.decompress(compressed_data)
    
    return decompressed_data