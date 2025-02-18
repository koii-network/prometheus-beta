import bz2
import os
from typing import Union

def compress_bzip2(input_data: Union[str, bytes], output_path: str = None, compression_level: int = 9) -> bytes:
    """
    Compress data using Bzip2 compression algorithm.
    
    Args:
        input_data (Union[str, bytes]): Data to be compressed. Can be a string or bytes.
        output_path (str, optional): Path to save the compressed file. If None, returns compressed bytes.
        compression_level (int, optional): Compression level from 1-9. Default is 9 (highest compression).
    
    Returns:
        bytes: Compressed data if no output_path is provided.
    
    Raises:
        ValueError: If compression level is not between 1 and 9.
        TypeError: If input_data is not str or bytes.
    """
    # Validate compression level
    if compression_level < 1 or compression_level > 9:
        raise ValueError("Compression level must be between 1 and 9")
    
    # Convert input to bytes if it's a string
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    elif not isinstance(input_data, bytes):
        raise TypeError("Input must be a string or bytes")
    
    # Compress data
    compressed_data = bz2.compress(input_data, compression_level)
    
    # Save to file if output_path is provided
    if output_path:
        with open(output_path, 'wb') as f:
            f.write(compressed_data)
    
    return compressed_data

def decompress_bzip2(input_data: Union[str, bytes], output_path: str = None) -> bytes:
    """
    Decompress Bzip2 compressed data.
    
    Args:
        input_data (Union[str, bytes]): Compressed data to be decompressed. Can be bytes or file path.
        output_path (str, optional): Path to save the decompressed file. If None, returns decompressed bytes.
    
    Returns:
        bytes: Decompressed data if no output_path is provided.
    
    Raises:
        TypeError: If input_data is not str, bytes, or file path.
    """
    # Read from file if input_data is a file path
    if isinstance(input_data, str) and os.path.isfile(input_data):
        with open(input_data, 'rb') as f:
            input_data = f.read()
    
    # Validate input type
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes or a valid file path")
    
    # Decompress data
    decompressed_data = bz2.decompress(input_data)
    
    # Save to file if output_path is provided
    if output_path:
        with open(output_path, 'wb') as f:
            f.write(decompressed_data)
    
    return decompressed_data