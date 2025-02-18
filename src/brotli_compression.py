import brotli
import typing

def compress_brotli(data: typing.Union[str, bytes], quality: int = 11) -> bytes:
    """
    Compress data using Brotli compression algorithm.
    
    Args:
        data (str or bytes): The data to compress
        quality (int, optional): Compression quality (0-11). Defaults to 11 (highest).
    
    Returns:
        bytes: Compressed data
    
    Raises:
        ValueError: If quality is out of range or data is invalid
        TypeError: If data is not str or bytes
    """
    # Validate input type
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be str or bytes")
    
    # Convert str to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate compression quality
    if not 0 <= quality <= 11:
        raise ValueError("Compression quality must be between 0 and 11")
    
    # Compress data
    try:
        return brotli.compress(data, quality)
    except Exception as e:
        raise ValueError(f"Compression failed: {str(e)}")

def decompress_brotli(compressed_data: bytes) -> bytes:
    """
    Decompress Brotli compressed data.
    
    Args:
        compressed_data (bytes): Brotli compressed data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        ValueError: If decompression fails
        TypeError: If input is not bytes
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress data
    try:
        return brotli.decompress(compressed_data)
    except Exception as e:
        raise ValueError(f"Decompression failed: {str(e)}")