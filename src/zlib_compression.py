import zlib
from typing import Union, Optional


def compress_data(data: Union[str, bytes], 
                  compression_level: Optional[int] = None) -> bytes:
    """
    Compress input data using Zlib compression algorithm.

    Args:
        data (Union[str, bytes]): The data to be compressed. 
            Can be a string or bytes object.
        compression_level (Optional[int], optional): Compression level from 0-9. 
            Defaults to None (default zlib compression level).
            0 = no compression, 9 = maximum compression

    Returns:
        bytes: Compressed data

    Raises:
        TypeError: If input is not str or bytes
        ValueError: If compression level is out of valid range
    """
    # Convert string to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be a string or bytes object")
    
    # Validate compression level if provided
    if compression_level is not None:
        if not isinstance(compression_level, int):
            raise TypeError("Compression level must be an integer")
        if compression_level < 0 or compression_level > 9:
            raise ValueError("Compression level must be between 0 and 9")
    
    # Perform compression
    try:
        if compression_level is None:
            return zlib.compress(data)
        else:
            return zlib.compress(data, compression_level)
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")


def decompress_data(compressed_data: bytes) -> bytes:
    """
    Decompress Zlib compressed data.

    Args:
        compressed_data (bytes): The data to be decompressed

    Returns:
        bytes: Decompressed data

    Raises:
        TypeError: If input is not bytes
        zlib.error: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be a bytes object")
    
    # Perform decompression
    try:
        return zlib.decompress(compressed_data)
    except zlib.error as e:
        raise zlib.error(f"Decompression failed: {str(e)}")