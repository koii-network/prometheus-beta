import os
import gzip
import shutil

def compress_file(input_path, output_path=None):
    """
    Compress a file using gzip compression.

    Args:
        input_path (str): Path to the input file to be compressed.
        output_path (str, optional): Path for the compressed output file. 
                                     If not provided, appends '.gz' to input path.

    Returns:
        str: Path to the compressed file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        IOError: If there are issues reading or writing files.
        ValueError: If input paths are invalid.
    """
    # Validate input path
    if not input_path or not isinstance(input_path, str):
        raise ValueError("Invalid input path")
    
    # Check if input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Determine output path if not provided
    if output_path is None:
        output_path = input_path + '.gz'
    
    # Ensure the directory for output exists
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    
    # Compress the file
    try:
        with open(input_path, 'rb') as f_in:
            with gzip.open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        return output_path
    except PermissionError:
        raise IOError(f"Permission denied when compressing file: {input_path}")
    except Exception as e:
        raise IOError(f"Error compressing file: {str(e)}")