import gzip
import os

def compress_file(input_file, output_file=None):
    """
    Compress a file using gzip compression.
    
    Args:
        input_file (str): Path to the input file to be compressed.
        output_file (str, optional): Path for the compressed output file. 
                                     If not provided, defaults to input_file + '.gz'
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If the input file does not exist
        PermissionError: If there are permission issues reading/writing files
        IOError: For other IO-related errors
    """
    # Validate input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist")
    
    # If no output file specified, create default output path
    if output_file is None:
        output_file = input_file + '.gz'
    
    # Perform compression
    try:
        with open(input_file, 'rb') as f_in:
            with gzip.open(output_file, 'wb') as f_out:
                f_out.writelines(f_in)
        
        return output_file
    
    except PermissionError:
        raise PermissionError(f"Permission denied when compressing {input_file}")
    except IOError as e:
        raise IOError(f"IO error occurred during compression: {str(e)}")