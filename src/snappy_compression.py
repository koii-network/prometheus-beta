import snappy

def compress_data(data):
    """
    Compress input data using Snappy compression algorithm.
    
    Args:
        data (bytes or str): The data to be compressed. 
                              If str is provided, it will be encoded to bytes.
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input is empty
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert to bytes if input is string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compress the data
    return snappy.compress(data)

def decompress_data(compressed_data):
    """
    Decompress Snappy compressed data.
    
    Args:
        compressed_data (bytes): The compressed data to be decompressed
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or invalid compressed data
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Input compressed data cannot be empty")
    
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress the data
    return snappy.decompress(compressed_data)