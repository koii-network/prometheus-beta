import lzma
import os

def compress_xz(input_path, output_path=None):
    """
    Compress a file using XZ compression algorithm.
    
    Args:
        input_path (str): Path to the input file to be compressed
        output_path (str, optional): Path for the compressed output file. 
                                     If not provided, appends '.xz' to input path
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues
        IOError: For other I/O related errors
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Set default output path if not provided
    if output_path is None:
        output_path = input_path + '.xz'
    
    try:
        # Perform XZ compression
        with open(input_path, 'rb') as input_file:
            with lzma.open(output_path, 'wb') as compressed_file:
                compressed_file.write(input_file.read())
        
        return output_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing {input_path} or {output_path}")
    except IOError as e:
        raise IOError(f"Error during XZ compression: {str(e)}")