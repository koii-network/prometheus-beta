import lzma
import os
from typing import Union, Optional

def compress_xz(input_data: Union[str, bytes], output_path: Optional[str] = None, compression_level: int = 6) -> bytes:
    """
    Compress data using XZ compression algorithm.
    
    Args:
        input_data (Union[str, bytes]): Data to be compressed. Can be a string or bytes.
        output_path (Optional[str]): Optional path to save the compressed file.
        compression_level (int): Compression level (0-9), default is 6.
    
    Returns:
        bytes: Compressed data
    
    Raises:
        ValueError: If input data is invalid or compression level is out of range
    """
    # Validate compression level
    if compression_level < 0 or compression_level > 9:
        raise ValueError("Compression level must be between 0 and 9")
    
    # Convert string to bytes if necessary
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Compress the data
    compressed_data = lzma.compress(input_data, preset=compression_level)
    
    # Optionally save to file if output path is provided
    if output_path:
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'wb') as f:
            f.write(compressed_data)
    
    return compressed_data

def decompress_xz(input_data: Union[str, bytes], output_path: Optional[str] = None) -> bytes:
    """
    Decompress XZ compressed data.
    
    Args:
        input_data (Union[str, bytes]): Compressed data to be decompressed. 
                                        Can be bytes or a path to a compressed file.
        output_path (Optional[str]): Optional path to save the decompressed file.
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        ValueError: If input data is invalid
        lzma.LZMAError: If decompression fails
    """
    # If input is a file path, read the compressed data
    if isinstance(input_data, str):
        with open(input_data, 'rb') as f:
            input_data = f.read()
    
    # Decompress the data
    decompressed_data = lzma.decompress(input_data)
    
    # Optionally save to file if output path is provided
    if output_path:
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'wb') as f:
            f.write(decompressed_data)
    
    return decompressed_data