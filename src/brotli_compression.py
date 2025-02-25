import brotli
from typing import Union

def compress_brotli(data: Union[str, bytes], quality: int = 11, 
                    mode: int = brotli.MODE_GENERIC) -> bytes:
    """
    Compress data using Brotli compression algorithm.

    Args:
        data (Union[str, bytes]): The input data to compress. 
            Can be a string or bytes object.
        quality (int, optional): Compression quality (0-11). 
            Defaults to 11 (highest compression).
        mode (int, optional): Compression mode. 
            Can be MODE_GENERIC, MODE_TEXT, or MODE_FONT.
            Defaults to MODE_GENERIC.

    Returns:
        bytes: Compressed data in Brotli format.

    Raises:
        ValueError: If compression quality is not between 0 and 11.
        TypeError: If input data is not str or bytes.
    """
    # Validate compression quality
    if not 0 <= quality <= 11:
        raise ValueError("Compression quality must be between 0 and 11")

    # Convert string to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be a string or bytes object")

    # Compress using Brotli
    try:
        return brotli.compress(data, mode=mode, quality=quality)
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def decompress_brotli(compressed_data: bytes) -> bytes:
    """
    Decompress Brotli-compressed data.

    Args:
        compressed_data (bytes): Brotli-compressed data.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        RuntimeError: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")

    # Decompress using Brotli
    try:
        return brotli.decompress(compressed_data)
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")