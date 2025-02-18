import bz2
import os

def compress_file_bzip2(input_file_path, output_file_path=None):
    """
    Compress a file using bzip2 compression.
    
    Args:
        input_file_path (str): Path to the input file to be compressed
        output_file_path (str, optional): Path to save the compressed file. 
                                          If not provided, appends '.bz2' to input file path.
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If the input file does not exist
        PermissionError: If there are permission issues reading/writing files
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # Determine output file path
    if output_file_path is None:
        output_file_path = input_file_path + '.bz2'
    
    try:
        # Read input file
        with open(input_file_path, 'rb') as input_file:
            data = input_file.read()
        
        # Compress data
        compressed_data = bz2.compress(data)
        
        # Write compressed data
        with open(output_file_path, 'wb') as output_file:
            output_file.write(compressed_data)
        
        return output_file_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when compressing file: {input_file_path}")