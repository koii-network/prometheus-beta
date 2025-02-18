import bz2
import os
from typing import Union, Optional

def compress_bzip2(data: Union[str, bytes], output_path: Optional[str] = None) -> bytes:
    """
    Compress data using Bzip2 compression algorithm.
    
    Args:
        data (Union[str, bytes]): The data to be compressed.
        output_path (Optional[str], optional): Path to save the compressed file. 
                                               If None, returns compressed bytes.
    
    Returns:
        bytes: Compressed data if no output path is provided.
        None: If output path is provided and file is saved successfully.
    
    Raises:
        TypeError: If input data is not str or bytes.
        IOError: If there's an error writing to the output file.
    """
    # Convert string to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be str or bytes")
    
    # Compress the data
    compressed_data = bz2.compress(data)
    
    # If output path is provided, write to file
    if output_path:
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            with open(output_path, 'wb') as f:
                f.write(compressed_data)
            return None
        except Exception as e:
            raise IOError(f"Error writing compressed data to {output_path}: {e}")
    
    return compressed_data

def decompress_bzip2(data: Union[str, bytes], output_path: Optional[str] = None) -> bytes:
    """
    Decompress Bzip2 compressed data.
    
    Args:
        data (Union[str, bytes]): The compressed data to be decompressed.
        output_path (Optional[str], optional): Path to save the decompressed file. 
                                               If None, returns decompressed bytes.
    
    Returns:
        bytes: Decompressed data if no output path is provided.
        None: If output path is provided and file is saved successfully.
    
    Raises:
        TypeError: If input data is not str or bytes.
        IOError: If there's an error writing to the output file.
        bz2.BZ2Error: If the input data is not valid Bzip2 compressed data.
    """
    # Convert string to bytes if needed
    if isinstance(data, str):
        # If it's a file path, read the file
        if os.path.isfile(data):
            with open(data, 'rb') as f:
                data = f.read()
        else:
            data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be str or bytes")
    
    # Decompress the data
    try:
        decompressed_data = bz2.decompress(data)
    except Exception as e:
        raise bz2.BZ2Error(f"Invalid Bzip2 compressed data: {e}")
    
    # If output path is provided, write to file
    if output_path:
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            with open(output_path, 'wb') as f:
                f.write(decompressed_data)
            return None
        except Exception as e:
            raise IOError(f"Error writing decompressed data to {output_path}: {e}")
    
    return decompressed_data