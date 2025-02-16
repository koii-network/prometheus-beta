import snappy

def snappy_compress(data):
    """
    Compress input data using Snappy compression algorithm.
    
    Args:
        data (bytes or str): The data to be compressed. 
                              If str is provided, it will be encoded to bytes.
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input data is empty
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert str to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Check input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compress the data
    try:
        compressed_data = snappy.compress(data)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def snappy_decompress(compressed_data):
    """
    Decompress data compressed with Snappy algorithm.
    
    Args:
        compressed_data (bytes): The compressed data to be decompressed
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input data is empty
        RuntimeError: If decompression fails
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Input compressed data cannot be empty")
    
    # Check input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress the data
    try:
        decompressed_data = snappy.decompress(compressed_data)
        return decompressed_data
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")