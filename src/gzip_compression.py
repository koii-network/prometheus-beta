import gzip
import os

def compress_file(input_file_path, output_file_path=None):
    """
    Compress a file using Gzip compression.
    
    Args:
        input_file_path (str): Path to the input file to be compressed
        output_file_path (str, optional): Path to save the compressed file. 
                                          If not provided, appends '.gz' to input file path.
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues reading/writing files
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # Determine output file path
    if output_file_path is None:
        output_file_path = input_file_path + '.gz'
    
    try:
        # Perform compression
        with open(input_file_path, 'rb') as f_in:
            with gzip.open(output_file_path, 'wb') as f_out:
                f_out.writelines(f_in)
        
        return output_file_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_file_path} or {output_file_path}")