import lzma
import os

def compress_file_xz(input_file_path, output_file_path=None):
    """
    Compress a file using XZ compression algorithm.
    
    Args:
        input_file_path (str): Path to the input file to be compressed
        output_file_path (str, optional): Path for the compressed file. 
                                          If not provided, appends '.xz' to input path
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues reading/writing files
        IOError: For other IO-related errors
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # Determine output file path
    if output_file_path is None:
        output_file_path = input_file_path + '.xz'
    
    try:
        # Open input file in binary read mode
        with open(input_file_path, 'rb') as input_file:
            # Open output file in binary write mode with XZ compression
            with lzma.open(output_file_path, 'wb', preset=9) as output_file:
                # Read and compress the entire file
                output_file.write(input_file.read())
        
        return output_file_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when compressing {input_file_path}")
    except IOError as e:
        raise IOError(f"Error compressing file: {str(e)}")