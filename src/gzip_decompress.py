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
        IOError: If there are issues reading or writing files
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file {input_path} does not exist")
    
    # Determine output path if not provided
    if output_path is None:
        output_path = input_path.removesuffix('.gz')
        if output_path == input_path:
            output_path += '_decompressed'
    
    # Perform decompression
    try:
        with gzip.open(input_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                f_out.write(f_in.read())
        
        return output_path
    except Exception as e:
        raise IOError(f"Error decompressing file: {str(e)}")