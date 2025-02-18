import bz2
import os
from typing import Union

def compress_file(input_path: str, output_path: Union[str, None] = None) -> str:
    """
    Compress a file using bzip2 compression.
    
    Args:
        input_path (str): Path to the input file to be compressed.
        output_path (str, optional): Path for the compressed output file. 
                                     If not provided, appends '.bz2' to input path.
    
    Returns:
        str: Path to the compressed file.
    
    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are insufficient permissions to read/write files.
        IsADirectoryError: If input_path is a directory instead of a file.
    """
    # Validate input file exists and is a file
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if os.path.isdir(input_path):
        raise IsADirectoryError(f"Input path is a directory, not a file: {input_path}")
    
    # Determine output path if not specified
    if output_path is None:
        output_path = input_path + '.bz2'
    
    # Perform compression
    try:
        with open(input_path, 'rb') as input_file:
            with bz2.open(output_path, 'wb') as compressed_file:
                compressed_file.write(input_file.read())
        
        return output_path
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to read {input_path} or write {output_path}")