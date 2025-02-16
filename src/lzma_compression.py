import lzma
import os

def compress_lzma(input_data, output_path=None):
    """
    Compress data using LZMA compression algorithm.
    
    Args:
        input_data (str or bytes): Data to be compressed. 
            If str, it will be encoded to bytes.
        output_path (str, optional): Path to save compressed file. 
            If None, returns compressed bytes.
    
    Returns:
        bytes or None: Compressed data or None if saved to file
    
    Raises:
        TypeError: If input is not str or bytes
        ValueError: If input is empty
        IOError: If there's an issue writing to file
    """
    # Validate input 
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Convert str to bytes if needed
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    elif not isinstance(input_data, bytes):
        raise TypeError("Input must be str or bytes")
    
    # Compress the data
    compressed_data = lzma.compress(input_data)
    
    # If output path is provided, save to file
    if output_path:
        try:
            with open(output_path, 'wb') as f:
                f.write(compressed_data)
            return None
        except IOError as e:
            raise IOError(f"Error writing to file {output_path}: {e}")
    
    return compressed_data

def decompress_lzma(input_data):
    """
    Decompress LZMA compressed data.
    
    Args:
        input_data (bytes or str): Compressed data or path to compressed file
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input is empty
        IOError: If there's an issue reading from file
    """
    # Validate input
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # If input is a file path, read the compressed data
    if isinstance(input_data, str):
        try:
            with open(input_data, 'rb') as f:
                input_data = f.read()
        except IOError as e:
            raise IOError(f"Error reading file {input_data}: {e}")
    
    # Validate input is bytes
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes or a valid file path")
    
    # Decompress the data
    return lzma.decompress(input_data)