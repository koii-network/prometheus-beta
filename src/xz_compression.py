import lzma
import os
from typing import Union, BinaryIO


def compress_xz(input_data: Union[str, bytes, BinaryIO], output_path: str = None, compression_level: int = 6) -> bytes:
    """
    Compress data using XZ compression algorithm.

    Args:
        input_data (Union[str, bytes, BinaryIO]): Data to compress. Can be a string, bytes, or file-like object.
        output_path (str, optional): Path to save compressed file. If None, returns compressed bytes.
        compression_level (int, optional): Compression level (0-9). Defaults to 6.

    Returns:
        bytes: Compressed data if no output path is provided.

    Raises:
        ValueError: If compression level is out of range.
        TypeError: If input_data is of unsupported type.
        IOError: If there are issues with file operations.
    """
    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")

    # Handle different input types
    if isinstance(input_data, str):
        data = input_data.encode('utf-8')
    elif isinstance(input_data, bytes):
        data = input_data
    elif hasattr(input_data, 'read'):
        data = input_data.read()
    else:
        raise TypeError("Input must be a string, bytes, or file-like object")

    # Compress the data
    compressed_data = lzma.compress(data, preset=compression_level)

    # If output path is provided, write to file
    if output_path:
        try:
            with open(output_path, 'wb') as f:
                f.write(compressed_data)
        except IOError as e:
            raise IOError(f"Error writing compressed file: {e}")
        return compressed_data

    return compressed_data


def decompress_xz(input_data: Union[str, bytes, BinaryIO], output_path: str = None) -> bytes:
    """
    Decompress XZ compressed data.

    Args:
        input_data (Union[str, bytes, BinaryIO]): Compressed data to decompress.
        output_path (str, optional): Path to save decompressed file. If None, returns decompressed bytes.

    Returns:
        bytes: Decompressed data if no output path is provided.

    Raises:
        lzma.LZMAError: If data cannot be decompressed.
        IOError: If there are issues with file operations.
    """
    # Handle different input types
    if isinstance(input_data, str):
        with open(input_data, 'rb') as f:
            data = f.read()
    elif isinstance(input_data, bytes):
        data = input_data
    elif hasattr(input_data, 'read'):
        data = input_data.read()
    else:
        raise TypeError("Input must be a string, bytes, or file-like object")

    # Decompress the data
    decompressed_data = lzma.decompress(data)

    # If output path is provided, write to file
    if output_path:
        try:
            with open(output_path, 'wb') as f:
                f.write(decompressed_data)
        except IOError as e:
            raise IOError(f"Error writing decompressed file: {e}")
        return decompressed_data

    return decompressed_data