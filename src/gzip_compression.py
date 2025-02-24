import gzip
import os
import shutil

def compress_file(input_path, output_path=None):
    """
    Compress a file using gzip compression.
    
    Args:
        input_path (str): Path to the input file to be compressed
        output_path (str, optional): Path for the compressed output file. 
                                     If not provided, appends '.gz' to input path.
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If the input file does not exist
        PermissionError: If there are permission issues reading/writing files
        IsADirectoryError: If input_path is a directory instead of a file
    """
    # Validate input file exists and is a file
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if os.path.isdir(input_path):
        raise IsADirectoryError(f"Input path must be a file, not a directory: {input_path}")
    
    # If no output path specified, create one by appending .gz
    if output_path is None:
        output_path = input_path + '.gz'
    
    # Compress the file
    try:
        with open(input_path, 'rb') as f_in:
            with gzip.open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        return output_path
    except PermissionError:
        raise PermissionError(f"Permission denied when compressing {input_path}")