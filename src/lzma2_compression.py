import lzma

def lzma2_compress(data):
    """
    Compress input data using LZMA2 compression algorithm.
    
    Args:
        data (bytes or str): The input data to be compressed.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert string to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Ensure input is bytes
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compress using LZMA2 (LZMA with advanced features)
    # LZMA preset 6 is a good balance between compression ratio and speed
    compressed_data = lzma.compress(data, preset=6)
    
    return compressed_data

def lzma2_decompress(compressed_data):
    """
    Decompress data compressed with LZMA2 compression algorithm.
    
    Args:
        compressed_data (bytes): The compressed data to be decompressed.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty or cannot be decompressed.
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    try:
        # Decompress the data
        decompressed_data = lzma.decompress(compressed_data)
        return decompressed_data
    except lzma.LZMAError as e:
        raise ValueError(f"Decompression failed: {str(e)}")