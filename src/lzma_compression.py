"""
LZMA Compression Utility

This module provides functionality for LZMA compression and decompression.
LZMA is a lossless data compression algorithm that provides high compression 
ratios and is used in 7z archive format.
"""

import lzma
from typing import Union, BinaryIO

def compress_lzma(data: Union[str, bytes], preset: int = 6) -> bytes:
    """
    Compress input data using LZMA compression algorithm.

    Args:
        data (Union[str, bytes]): The input data to compress. 
            Can be a string or bytes object.
        preset (int, optional): Compression level from 0-9. 
            Defaults to 6 (balanced compression).

    Returns:
        bytes: Compressed data in LZMA format.

    Raises:
        TypeError: If input is not str or bytes.
        ValueError: If preset is not between 0 and 9.
    """
    # Validate input type
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be str or bytes")
    
    # Validate compression preset
    if not 0 <= preset <= 9:
        raise ValueError("Compression preset must be between 0 and 9")
    
    # Convert string to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Compress data using LZMA
    try:
        return lzma.compress(data, preset=preset)
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def decompress_lzma(compressed_data: bytes) -> bytes:
    """
    Decompress LZMA compressed data.

    Args:
        compressed_data (bytes): LZMA compressed data.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        lzma.LZMAError: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress data using LZMA
    try:
        return lzma.decompress(compressed_data)
    except lzma.LZMAError as e:
        raise lzma.LZMAError(f"Decompression failed: {str(e)}")