import gzip
import os
import shutil

def decompress_gzip_file(input_filepath, output_filepath=None):
    """
    Decompress a gzip file to a specified output path.

    Args:
        input_filepath (str): Path to the input .gz file
        output_filepath (str, optional): Path to save the decompressed file. 
                                         If not provided, removes .gz extension.

    Returns:
        str: Path to the decompressed file

    Raises:
        FileNotFoundError: If input file does not exist
        IOError: If there are issues reading or writing files
        ValueError: If input file is not a .gz file
    """
    # Validate input file exists and is a .gz file
    if not os.path.exists(input_filepath):
        raise FileNotFoundError(f"Input file not found: {input_filepath}")
    
    if not input_filepath.endswith('.gz'):
        raise ValueError(f"Input file must be a .gz file: {input_filepath}")

    # Determine output filepath if not provided
    if output_filepath is None:
        output_filepath = input_filepath[:-3]  # Remove .gz extension

    try:
        # Open gzip file and decompress to output file
        with gzip.open(input_filepath, 'rb') as f_in:
            with open(output_filepath, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        return output_filepath
    except IOError as e:
        raise IOError(f"Error decompressing file: {e}")