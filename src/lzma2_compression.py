import lzma
import io
from typing import Union, BinaryIO

def compress_lzma2(data: Union[str, bytes], compression_level: int = 6) -> bytes:
    """
    Compress input data using LZMA compression algorithm.

    Args:
        data (Union[str, bytes]): Input data to compress. 
                                   Strings will be encoded to UTF-8 bytes.
        compression_level (int, optional): Compression level from 0-9. 
                                           Defaults to 6 (medium compression).

    Returns:
        bytes: Compressed data in LZMA format.

    Raises:
        ValueError: If compression level is not between 0 and 9.
        TypeError: If input data is not str or bytes.
    """
    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")

    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif not isinstance(data, bytes):
        raise TypeError("Input must be string or bytes")

    # Compress using LZMA
    try:
        # Use standard LZMA compression with specified filter
        compressed = lzma.compress(data, preset=compression_level)
        return compressed
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def decompress_lzma2(compressed_data: bytes) -> bytes:
    """
    Decompress LZMA compressed data.

    Args:
        compressed_data (bytes): LZMA compressed data to decompress.

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

    # Decompress using LZMA
    try:
        decompressed = lzma.decompress(compressed_data)
        return decompressed
    except lzma.LZMAError as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")