import os
import bz2

def compress_file_bzip2(input_file, output_file=None):
    """
    Compress a file using bzip2 compression.
    
    Args:
        input_file (str): Path to the input file to be compressed
        output_file (str, optional): Path for the compressed output file. 
                                     If not provided, defaults to input_file + '.bz2'
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If the input file does not exist
        PermissionError: If there are permission issues
        IOError: For other IO-related errors
    """
    # Validate input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist")
    
    # If no output file specified, create default output filename
    if output_file is None:
        output_file = input_file + '.bz2'
    
    try:
        # Open input file for reading
        with open(input_file, 'rb') as input_handle:
            # Open output file for writing compressed data
            with bz2.open(output_file, 'wb') as output_handle:
                # Read input file in chunks and compress
                chunk = input_handle.read(64 * 1024)  # 64KB chunks
                while chunk:
                    output_handle.write(chunk)
                    chunk = input_handle.read(64 * 1024)
        
        return output_file
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing {input_file} or {output_file}")
    except IOError as e:
        raise IOError(f"Error compressing file: {e}")