import snappy

def snappy_compress(data):
    """
    Compress input data using Snappy compression algorithm.
    
    Args:
        data (bytes or str): The input data to compress.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Compress using Snappy
    return snappy.compress(data)

def snappy_decompress(compressed_data):
    """
    Decompress data that was compressed with Snappy.
    
    Args:
        compressed_data (bytes): The compressed data to decompress.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty or invalid.
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    # Decompress using Snappy
    return snappy.decompress(compressed_data)