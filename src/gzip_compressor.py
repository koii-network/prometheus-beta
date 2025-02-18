import gzip
import os

def compress_file(input_file, output_file=None):
    """
    Compress a file using gzip compression.
    
    Args:
        input_file (str): Path to the input file to be compressed
        output_file (str, optional): Path for the compressed output file. 
                                     If not provided, appends .gz to input filename
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues
        IsADirectoryError: If input_file is a directory
    """
    # Validate input file exists and is a file
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist")
    
    if os.path.isdir(input_file):
        raise IsADirectoryError(f"Input path {input_file} is a directory, not a file")
    
    # Determine output file path
    if output_file is None:
        output_file = input_file + '.gz'
    
    try:
        # Compress the file
        with open(input_file, 'rb') as f_in:
            with gzip.open(output_file, 'wb') as f_out:
                f_out.writelines(f_in)
        
        return output_file
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to compress {input_file}")