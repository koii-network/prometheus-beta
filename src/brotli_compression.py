import brotli

def compress_with_brotli(data: bytes, quality: int = 11, mode: int = 0) -> bytes:
    """
    Compress data using Brotli compression algorithm.
    
    Args:
        data (bytes): The input data to compress
        quality (int, optional): Compression quality (0-11). 
                                 Defaults to 11 (maximum compression).
        mode (int, optional): Compression mode. 
                               0: MODE_GENERIC (default)
                               1: MODE_TEXT (UTF-8 text)
                               2: MODE_FONT (WOFF 2.0)
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If quality or mode is out of range
    """
    # Validate input types
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    # Validate compression quality
    if not 0 <= quality <= 11:
        raise ValueError("Compression quality must be between 0 and 11")
    
    # Validate compression mode
    if mode not in [0, 1, 2]:
        raise ValueError("Compression mode must be 0 (GENERIC), 1 (TEXT), or 2 (FONT)")
    
    # Perform Brotli compression
    compressed_data = brotli.compress(data, mode=mode, quality=quality)
    
    return compressed_data

def decompress_with_brotli(compressed_data: bytes) -> bytes:
    """
    Decompress Brotli compressed data.
    
    Args:
        compressed_data (bytes): The Brotli compressed data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        brotli.Error: If decompression fails
    """
    # Validate input types
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Perform Brotli decompression
    decompressed_data = brotli.decompress(compressed_data)
    
    return decompressed_data