import snappy

def compress_data(data):
    """
    Compress input data using Snappy compression algorithm.
    
    Args:
        data (bytes or str): Data to be compressed. If str, it will be encoded to bytes.
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input is empty
    """
    # Validate input
    if data is None:
        raise ValueError("Input data cannot be None")
    
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Check input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Check for empty input
    if len(data) == 0:
        raise ValueError("Input data cannot be empty")
    
    # Compress the data
    return snappy.compress(data)

def decompress_data(compressed_data):
    """
    Decompress Snappy compressed data.
    
    Args:
        compressed_data (bytes): Compressed data to be decompressed
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or cannot be decompressed
    """
    # Validate input
    if compressed_data is None:
        raise ValueError("Compressed data cannot be None")
    
    # Check input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Check for empty input
    if len(compressed_data) == 0:
        raise ValueError("Compressed data cannot be empty")
    
    # Decompress the data
    try:
        return snappy.decompress(compressed_data)
    except Exception as e:
        raise ValueError(f"Decompression failed: {str(e)}")