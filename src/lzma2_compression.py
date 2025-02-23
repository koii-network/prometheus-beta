import lzma
import io
from typing import Union, BinaryIO

def compress_lzma2(data: Union[str, bytes], preset: int = 6) -> bytes:
    """
    Compress data using LZMA2 compression algorithm.

    Args:
        data (Union[str, bytes]): The input data to compress. 
            Can be a string or bytes object.
        preset (int, optional): Compression level from 0-9. 
            Defaults to 6 (balanced compression).

    Returns:
        bytes: Compressed data.

    Raises:
        ValueError: If compression preset is out of range.
        TypeError: If input data is not str or bytes.
    """
    # Validate compression preset
    if not 0 <= preset <= 9:
        raise ValueError("Compression preset must be between 0 and 9")

    # Convert string to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be a string or bytes object")

    # Compress using LZMA with specified preset
    try:
        # Use LZMA2 compression with specified preset
        compressed = lzma.compress(data, format=lzma.FORMAT_ALONE, preset=preset)
        return compressed
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def decompress_lzma2(compressed_data: bytes) -> bytes:
    """
    Decompress LZMA2 compressed data.

    Args:
        compressed_data (bytes): The LZMA2 compressed data.

    Returns:
        bytes: Decompressed data.

    Raises:
        ValueError: If input is not bytes or is empty.
        lzma.LZMAError: If decompression fails.
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")

    try:
        # Decompress using LZMA
        decompressed = lzma.decompress(compressed_data, format=lzma.FORMAT_ALONE)
        return decompressed
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")