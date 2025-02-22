import gzip
import os
import shutil

def compress_file(input_file_path, output_file_path=None):
    """
    Compress a file using gzip compression.
    
    Args:
        input_file_path (str): Path to the input file to be compressed
        output_file_path (str, optional): Path to save the compressed file. 
                                          If not provided, appends '.gz' to input file path.
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # If no output path specified, create one by appending .gz
    if output_file_path is None:
        output_file_path = input_file_path + '.gz'
    
    try:
        # Open input file for reading
        with open(input_file_path, 'rb') as f_in:
            # Open gzip compressed file for writing
            with gzip.open(output_file_path, 'wb') as f_out:
                # Copy contents, compressing as we go
                shutil.copyfileobj(f_in, f_out)
        
        return output_file_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when compressing file: {input_file_path}")