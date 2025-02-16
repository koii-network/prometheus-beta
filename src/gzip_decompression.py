import gzip
import os

def decompress_gzip_file(input_file, output_file=None):
    """
    Decompress a gzip file to a specified output file or to a file with .gz removed.
    
    Args:
        input_file (str): Path to the input gzip file
        output_file (str, optional): Path to the output decompressed file. 
                                     If not provided, uses input filename without .gz extension
    
    Returns:
        str: Path to the decompressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        IOError: If there are issues reading or writing files
    """
    # Validate input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist")
    
    # Determine output file path if not provided
    if output_file is None:
        output_file = input_file.removesuffix('.gz')
        if output_file == input_file:
            output_file += '.decompressed'
    
    # Open input gzip file and decompress to output file
    try:
        with gzip.open(input_file, 'rb') as f_in:
            with open(output_file, 'wb') as f_out:
                f_out.write(f_in.read())
    except Exception as e:
        raise IOError(f"Error decompressing file: {e}")
    
    return output_file