import brotli

def compress_brotli(data, quality=11):
    """
    Compress data using Brotli compression algorithm.
    
    Args:
        data (bytes or str): The data to be compressed.
        quality (int, optional): Compression level from 0-11. 
                                 Default is 11 (highest compression).
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If compression quality is out of range
    """
    # Convert str to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Validate compression quality
    if quality < 0 or quality > 11:
        raise ValueError("Compression quality must be between 0 and 11")
    
    # Compress data using Brotli
    return brotli.compress(data, quality)

def decompress_brotli(compressed_data):
    """
    Decompress data using Brotli decompression algorithm.
    
    Args:
        compressed_data (bytes): The Brotli-compressed data to decompress.
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        brotli.Error: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress data using Brotli
    return brotli.decompress(compressed_data)