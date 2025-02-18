import lz4.frame

def compress_lz4(data):
    """
    Compress input data using LZ4 compression algorithm.
    
    Args:
        data (bytes or str): Data to be compressed. 
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
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Validate input is not empty
    if len(data) == 0:
        raise ValueError("Input data cannot be empty")
    
    # Compress data using LZ4 frame compression
    return lz4.frame.compress(data)

def decompress_lz4(compressed_data):
    """
    Decompress LZ4 compressed data.
    
    Args:
        compressed_data (bytes): LZ4 compressed data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or cannot be decompressed
    """
    # Validate input
    if compressed_data is None:
        raise ValueError("Compressed data cannot be None")
    
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Validate input is not empty
    if len(compressed_data) == 0:
        raise ValueError("Compressed data cannot be empty")
    
    # Decompress data using LZ4 frame decompression
    try:
        return lz4.frame.decompress(compressed_data)
    except Exception as e:
        raise ValueError(f"Decompression failed: {str(e)}")