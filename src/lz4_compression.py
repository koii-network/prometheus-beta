import lz4.frame

def lz4_compress(data):
    """
    Compress data using LZ4 compression algorithm.
    
    Args:
        data (bytes or str): The input data to compress.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or str.
    """
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compress using LZ4 frame compression
    compressed_data = lz4.frame.compress(data)
    
    return compressed_data

def lz4_decompress(compressed_data):
    """
    Decompress data previously compressed with LZ4.
    
    Args:
        compressed_data (bytes): The compressed data to decompress.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        lz4.frame.LZ4FrameError: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress using LZ4 frame decompression
    decompressed_data = lz4.frame.decompress(compressed_data)
    
    return decompressed_data