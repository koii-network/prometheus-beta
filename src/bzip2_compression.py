import bz2
import os
from typing import Union, Optional

def compress_bzip2(input_data: Union[str, bytes], output_path: Optional[str] = None) -> bytes:
    """
    Compress data using Bzip2 compression algorithm.

    Args:
        input_data (Union[str, bytes]): Data to be compressed. 
            Can be a string or bytes object.
        output_path (Optional[str]): Optional path to save compressed file.
            If None, returns compressed bytes.

    Returns:
        bytes: Compressed data

    Raises:
        TypeError: If input is not str or bytes
        ValueError: If input is empty
        IOError: If there's an issue writing to output file
    """
    # Handle None input
    if input_data is None:
        raise TypeError("Input cannot be None")
    
    # Validate input
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Convert string to bytes if necessary
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    elif not isinstance(input_data, bytes):
        raise TypeError("Input must be str or bytes")
    
    # Compress data
    compressed_data = bz2.compress(input_data)
    
    # Write to file if output path is provided
    if output_path:
        try:
            with open(output_path, 'wb') as f:
                f.write(compressed_data)
        except IOError as e:
            raise IOError(f"Error writing to file {output_path}: {e}")
    
    return compressed_data

def decompress_bzip2(input_data: Union[str, bytes], output_path: Optional[str] = None) -> bytes:
    """
    Decompress Bzip2 compressed data.

    Args:
        input_data (Union[str, bytes]): Compressed data to decompress. 
            Can be a string (file path) or bytes object.
        output_path (Optional[str]): Optional path to save decompressed file.
            If None, returns decompressed bytes.

    Returns:
        bytes: Decompressed data

    Raises:
        TypeError: If input is not str or bytes
        ValueError: If input is empty
        IOError: If there's an issue reading/writing files
        Exception: If data cannot be decompressed
    """
    # Handle None input
    if input_data is None:
        raise TypeError("Input cannot be None")
    
    # Handle file input
    if isinstance(input_data, str):
        try:
            with open(input_data, 'rb') as f:
                input_data = f.read()
        except IOError as e:
            raise IOError(f"Error reading file {input_data}: {e}")
    
    # Validate input
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be str (file path) or bytes")
    
    # Decompress data
    try:
        decompressed_data = bz2.decompress(input_data)
    except Exception as e:
        raise Exception(f"Decompression failed: {e}")
    
    # Write to file if output path is provided
    if output_path:
        try:
            with open(output_path, 'wb') as f:
                f.write(decompressed_data)
        except IOError as e:
            raise IOError(f"Error writing to file {output_path}: {e}")
    
    return decompressed_data