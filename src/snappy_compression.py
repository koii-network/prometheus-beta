import snappy

def compress_data(data):
    """
    Compress input data using the Snappy compression algorithm.

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
    
    # Compress data using Snappy
    try:
        compressed_data = snappy.compress(data)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def decompress_data(compressed_data):
    """
    Decompress Snappy-compressed data.

    Args:
        compressed_data (bytes): The compressed data to decompress.

    Returns:
        bytes: Decompressed data

    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty
        RuntimeError: If decompression fails
    """
    # Validate input
    if compressed_data is None:
        raise ValueError("Compressed data cannot be None")
    
    # Check input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Check for empty input
    if len(compressed_data) == 0:
        raise ValueError("Compressed data cannot be empty")
    
    # Decompress data using Snappy
    try:
        decompressed_data = snappy.decompress(compressed_data)
        return decompressed_data
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")