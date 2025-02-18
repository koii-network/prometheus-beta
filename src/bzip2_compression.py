import bz2
import os
from typing import Union

def compress_bzip2(input_data: Union[str, bytes], output_path: str = None) -> bytes:
    """
    Compress data using Bzip2 compression algorithm.
    
    Args:
        input_data (Union[str, bytes]): The data to be compressed. 
                                        Can be a string or bytes object.
        output_path (str, optional): Path to save the compressed file. 
                                     If None, returns compressed bytes.
    
    Returns:
        bytes: Compressed data if no output path is provided.
        None: If output path is provided and file is saved successfully.
    
    Raises:
        TypeError: If input_data is not str or bytes.
        IOError: If there's an error writing to the output file.
    """
    # Convert string to bytes if necessary
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Validate input type
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be a string or bytes object")
    
    # Compress the data
    compressed_data = bz2.compress(input_data)
    
    # If output path is provided, write to file
    if output_path:
        try:
            with open(output_path, 'wb') as f:
                f.write(compressed_data)
            return None
        except IOError as e:
            raise IOError(f"Error writing to output file: {e}")
    
    return compressed_data

def decompress_bzip2(input_data: Union[str, bytes], output_path: str = None) -> bytes:
    """
    Decompress Bzip2 compressed data.
    
    Args:
        input_data (Union[str, bytes]): Compressed data to decompress. 
                                        Can be a string or bytes object.
        output_path (str, optional): Path to save the decompressed file. 
                                     If None, returns decompressed bytes.
    
    Returns:
        bytes: Decompressed data if no output path is provided.
        None: If output path is provided and file is saved successfully.
    
    Raises:
        TypeError: If input_data is not str or bytes.
        IOError: If there's an error writing to the output file.
        bz2.BZ2Error: If the input data is not valid Bzip2 compressed data.
    """
    # If input is a file path, read the file
    if isinstance(input_data, str) and os.path.isfile(input_data):
        with open(input_data, 'rb') as f:
            input_data = f.read()
    
    # Convert string to bytes if necessary
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Validate input type
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be a string, bytes object, or valid file path")
    
    # Decompress the data
    try:
        decompressed_data = bz2.decompress(input_data)
    except bz2.BZ2Error as e:
        raise bz2.BZ2Error(f"Invalid Bzip2 compressed data: {e}")
    
    # If output path is provided, write to file
    if output_path:
        try:
            with open(output_path, 'wb') as f:
                f.write(decompressed_data)
            return None
        except IOError as e:
            raise IOError(f"Error writing to output file: {e}")
    
    return decompressed_data