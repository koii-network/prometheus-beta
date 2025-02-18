import gzip
import os

def decompress_gzip_file(input_file_path, output_file_path=None):
    """
    Decompress a gzip file to a specified output path or to the same directory as the input file.
    
    Args:
        input_file_path (str): Path to the input .gz file
        output_file_path (str, optional): Path to save the decompressed file. 
                                          If not provided, saves in the same directory as input file.
    
    Returns:
        str: Path to the decompressed file
    
    Raises:
        FileNotFoundError: If the input file does not exist
        ValueError: If the input file is not a .gz file
    """
    # Validate input file path
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # Validate file extension
    if not input_file_path.endswith('.gz'):
        raise ValueError(f"Input file must be a .gz file: {input_file_path}")
    
    # Determine output file path if not provided
    if output_file_path is None:
        output_file_path = input_file_path.rstrip('.gz')
    
    # Decompress the file
    try:
        with gzip.open(input_file_path, 'rb') as f_in:
            with open(output_file_path, 'wb') as f_out:
                f_out.write(f_in.read())
        
        return output_file_path
    
    except Exception as e:
        raise RuntimeError(f"Error decompressing file: {str(e)}")