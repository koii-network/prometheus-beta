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
        PermissionError: If there are permission issues writing the output file
        ValueError: If input file is not a gzip file
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Determine output path if not provided
    if output_path is None:
        output_path = input_path.removesuffix('.gz')
    
    try:
        # Open and read the gzip file
        with gzip.open(input_path, 'rb') as f_in:
            # Write the decompressed content to output file
            with open(output_path, 'wb') as f_out:
                f_out.write(f_in.read())
        
        return output_path
    
    except gzip.BadGzipFile:
        raise ValueError(f"Input file is not a valid gzip file: {input_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied when writing to: {output_path}")