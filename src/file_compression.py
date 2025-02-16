import bz2
import os

def compress_file_bzip2(input_path, output_path=None):
    """
    Compress a file using bzip2 compression.
    
    Args:
        input_path (str): Path to the input file to be compressed
        output_path (str, optional): Path for the output compressed file. 
                                     If not provided, appends '.bz2' to input path
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues
        IsADirectoryError: If input path is a directory
    """
    # Validate input file exists and is a file
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if os.path.isdir(input_path):
        raise IsADirectoryError(f"Input path is a directory, not a file: {input_path}")
    
    # Determine output path
    if output_path is None:
        output_path = input_path + '.bz2'
    
    # Read input file and compress
    try:
        with open(input_path, 'rb') as input_file:
            data = input_file.read()
        
        compressed_data = bz2.compress(data)
        
        with open(output_path, 'wb') as output_file:
            output_file.write(compressed_data)
        
        return output_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when compressing file: {input_path}")