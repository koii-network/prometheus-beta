import gzip
import os
import shutil

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
        IOError: If there are issues reading or writing files
    """
    # Validate input file has .gz extension first
    if not input_path.lower().endswith('.gz'):
        raise ValueError(f"Input file must be a .gz file: {input_path}")

    # Then validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Determine output path if not specified
    if output_path is None:
        output_path = input_path[:-3]  # Remove .gz extension

    try:
        # Open and decompress the file
        with gzip.open(input_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        return output_path

    except PermissionError:
        raise IOError(f"Permission denied when writing to {output_path}")
    except Exception as e:
        raise IOError(f"Error decompressing file: {str(e)}")