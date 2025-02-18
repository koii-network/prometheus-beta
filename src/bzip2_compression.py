import bz2
from typing import Union

def compress_bzip2(data: Union[str, bytes], compression_level: int = 9) -> bytes:
    """
    Compress data using Bzip2 compression algorithm.

    Args:
        data (Union[str, bytes]): The data to be compressed.
        compression_level (int, optional): Compression level from 1-9. 
                                           Defaults to 9 (highest compression).

    Returns:
        bytes: Compressed data.

    Raises:
        ValueError: If compression level is not between 1 and 9.
        TypeError: If input data is not str or bytes.
    """
    # Validate compression level
    if compression_level < 1 or compression_level > 9:
        raise ValueError("Compression level must be between 1 and 9")

    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be a string or bytes")

    # Compress the data
    compressed_data = bz2.compress(data, compression_level)
    return compressed_data

def decompress_bzip2(compressed_data: bytes) -> bytes:
    """
    Decompress Bzip2 compressed data.

    Args:
        compressed_data (bytes): The data to be decompressed.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        bz2.BZ2Error: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")

    # Decompress the data
    decompressed_data = bz2.decompress(compressed_data)
    return decompressed_data