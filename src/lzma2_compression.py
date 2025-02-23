import lzma
import io
from typing import Union, BinaryIO

def compress_lzma2(data: Union[str, bytes], preset: int = 6) -> bytes:
    """
    Compress data using LZMA2 compression algorithm.

    Args:
        data (Union[str, bytes]): The input data to compress.
        preset (int, optional): Compression level (0-9). Defaults to 6.

    Raises:
        ValueError: If preset is not between 0 and 9
        TypeError: If input data is not str or bytes

    Returns:
        bytes: Compressed data
    """
    # Validate compression preset
    if not 0 <= preset <= 9:
        raise ValueError("Compression preset must be between 0 and 9")

    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif not isinstance(data, bytes):
        raise TypeError("Input must be str or bytes")

    # Use LZMA2 compression with specified preset
    try:
        # LZMA2 uses the preset parameter for compression level
        compressed = lzma.compress(data, preset=preset | lzma.PRESET_EXTREME)
        return compressed
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def decompress_lzma2(compressed_data: bytes) -> bytes:
    """
    Decompress LZMA2 compressed data.

    Args:
        compressed_data (bytes): The compressed input data.

    Raises:
        TypeError: If input is not bytes
        lzma.LZMAError: If decompression fails

    Returns:
        bytes: Decompressed data
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")

    try:
        # Decompress the LZMA2 compressed data
        decompressed = lzma.decompress(compressed_data)
        return decompressed
    except lzma.LZMAError as e:
        raise lzma.LZMAError(f"Decompression failed: {str(e)}")