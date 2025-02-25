import lzma
import typing

def compress_lzma(data: typing.Union[str, bytes], preset: int = 6) -> bytes:
    """
    Compress input data using LZMA compression algorithm.

    Args:
        data (str or bytes): The input data to compress. 
                              If str, it will be encoded to UTF-8 bytes.
        preset (int, optional): Compression level from 0-9. 
                                Defaults to 6 (default LZMA compression level).

    Returns:
        bytes: Compressed data

    Raises:
        TypeError: If input is not str or bytes
        ValueError: If preset is not between 0 and 9
    """
    # Validate input type
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be str or bytes")
    
    # Validate compression preset
    if not 0 <= preset <= 9:
        raise ValueError("Compression preset must be between 0 and 9")
    
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Compress using LZMA
    return lzma.compress(data, preset=preset)

def decompress_lzma(compressed_data: bytes) -> bytes:
    """
    Decompress LZMA compressed data.

    Args:
        compressed_data (bytes): LZMA compressed data to decompress

    Returns:
        bytes: Decompressed data

    Raises:
        TypeError: If input is not bytes
        lzma.LZMAError: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress using LZMA
    return lzma.decompress(compressed_data)