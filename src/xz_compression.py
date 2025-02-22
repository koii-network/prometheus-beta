import lzma
import os
from typing import Union

def compress_xz(input_data: Union[str, bytes], output_path: str = None, compression_level: int = 6) -> bytes:
    """
    Compress data using XZ compression algorithm.
    
    Args:
        input_data (str or bytes): Data to compress. Can be a string or bytes.
        output_path (str, optional): Path to save the compressed file. If None, returns compressed bytes.
        compression_level (int, optional): Compression level (0-9). Defaults to 6.
    
    Returns:
        bytes: Compressed data if no output_path is provided.
    
    Raises:
        ValueError: If compression level is not between 0 and 9.
        TypeError: If input_data is not str or bytes.
    """
    # Validate compression level
    if compression_level < 0 or compression_level > 9:
        raise ValueError("Compression level must be between 0 and 9")
    
    # Validate input data type
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    elif not isinstance(input_data, bytes):
        raise TypeError("Input must be str or bytes")
    
    # Compress the data
    compressed_data = lzma.compress(input_data, preset=compression_level)
    
    # If output path is provided, save to file
    if output_path:
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'wb') as f:
            f.write(compressed_data)
    
    return compressed_data

def decompress_xz(input_data: Union[str, bytes], output_path: str = None) -> bytes:
    """
    Decompress XZ compressed data.
    
    Args:
        input_data (str or bytes): Compressed data to decompress. Can be bytes or file path.
        output_path (str, optional): Path to save the decompressed file. If None, returns decompressed bytes.
    
    Returns:
        bytes: Decompressed data if no output_path is provided.
    
    Raises:
        TypeError: If input_data is not str, bytes, or file path.
    """
    # If input is a file path, read the file
    if isinstance(input_data, str) and os.path.isfile(input_data):
        with open(input_data, 'rb') as f:
            input_data = f.read()
    
    # Validate input data type
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes or a valid file path")
    
    # Decompress the data
    decompressed_data = lzma.decompress(input_data)
    
    # If output path is provided, save to file
    if output_path:
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'wb') as f:
            f.write(decompressed_data)
    
    return decompressed_data