import gzip
import os
import shutil

def compress_file(input_file_path, output_file_path=None):
    """
    Compress a file using gzip compression.
    
    :param input_file_path: Path to the input file to be compressed
    :param output_file_path: Optional path for the compressed file. 
                              If not provided, appends .gz to the input file path
    :return: Path to the compressed file
    :raises FileNotFoundError: If the input file does not exist
    :raises PermissionError: If there are permission issues
    :raises IOError: For other IO-related errors
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # If no output path specified, create one by appending .gz
    if output_file_path is None:
        output_file_path = input_file_path + '.gz'
    
    try:
        # Open input file for reading
        with open(input_file_path, 'rb') as f_in:
            # Open gzip compressed output file
            with gzip.open(output_file_path, 'wb') as f_out:
                # Copy contents with compression
                shutil.copyfileobj(f_in, f_out)
        
        return output_file_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when compressing {input_file_path}")
    except IOError as e:
        raise IOError(f"Error compressing file: {str(e)}")