import gzip
import os

def decompress_gzip_file(input_path, output_path=None):
    """
    Decompress a gzip file to a specified output path.
    
    Args:
        input_path (str): Path to the input .gz file
        output_path (str, optional): Path to save the decompressed file. 
                                     If not provided, uses input path without .gz extension
    
    Returns:
        str: Path to the decompressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        ValueError: If input file is not a .gz file
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Validate input file is a .gz file
    if not input_path.endswith('.gz'):
        raise ValueError(f"Input file must be a .gz file: {input_path}")
    
    # Determine output path if not provided
    if output_path is None:
        output_path = input_path[:-3]  # Remove .gz extension
    
    # Decompress the file
    try:
        with gzip.open(input_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                f_out.write(f_in.read())
        
        return output_path
    except Exception as e:
        raise IOError(f"Error decompressing file: {str(e)}")