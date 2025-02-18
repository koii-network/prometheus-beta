import gzip
import os

def decompress_gzip_file(input_path, output_path=None):
    """
    Decompress a gzip file.
    
    Args:
        input_path (str): Path to the input .gz file
        output_path (str, optional): Path to save the decompressed file. 
                                     If not provided, uses input filename without .gz extension
    
    Returns:
        str: Path to the decompressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        ValueError: If input file is not a .gz file
        IOError: If there are issues reading or writing files
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Validate input is a .gz file
    if not input_path.endswith('.gz'):
        raise ValueError(f"Input file must be a .gz file: {input_path}")
    
    # Determine output path if not provided
    if output_path is None:
        output_path = input_path[:-3]  # Remove .gz extension
    
    try:
        # Open and read the gzipped file
        with gzip.open(input_path, 'rb') as f_in:
            # Write the decompressed content to output file
            with open(output_path, 'wb') as f_out:
                f_out.write(f_in.read())
        
        return output_path
    
    except IOError as e:
        raise IOError(f"Error during gzip decompression: {str(e)}")