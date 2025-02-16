import gzip
import os
import shutil

def compress_file(input_path, output_path=None):
    """
    Compress a file using gzip compression.

    Args:
        input_path (str): Path to the input file to be compressed
        output_path (str, optional): Path for the compressed output file. 
                                     If not provided, appends .gz to input path.

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

    # If no output path provided, generate one by appending .gz
    if output_path is None:
        output_path = input_path + '.gz'

    try:
        # Open input file for reading and output file for gzip compression
        with open(input_path, 'rb') as f_in:
            with gzip.open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        return output_path
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to compress {input_path}")