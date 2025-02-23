import gzip
import os

def compress_file(input_path, output_path=None):
    """
    Compress a file using gzip compression.
    
    Args:
        input_path (str): Path to the input file to be compressed
        output_path (str, optional): Path for the compressed output file. 
                                     If not provided, appends .gz to input path.
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues
        ValueError: If input or output paths are invalid
    """
    # Validate input path
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Determine output path
    if output_path is None:
        output_path = input_path + '.gz'
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True) if os.path.dirname(output_path) else None
    
    try:
        # Perform compression
        with open(input_path, 'rb') as f_in:
            with gzip.open(output_path, 'wb') as f_out:
                f_out.writelines(f_in)
        
        return output_path
    except PermissionError:
        raise PermissionError(f"Permission denied when compressing {input_path}")
    except Exception as e:
        raise ValueError(f"Compression error: {str(e)}")