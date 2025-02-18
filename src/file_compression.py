import bz2
import os

def compress_file_bzip2(input_file_path, output_file_path=None):
    """
    Compress a file using bzip2 compression.
    
    :param input_file_path: Path to the input file to be compressed
    :param output_file_path: Optional path for the compressed file. 
                              If not provided, appends '.bz2' to the input file path
    :return: Path to the compressed file
    :raises FileNotFoundError: If input file does not exist
    :raises PermissionError: If there are permission issues
    :raises IOError: For other I/O related errors
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file {input_file_path} does not exist")
    
    # Set default output path if not provided
    if output_file_path is None:
        output_file_path = input_file_path + '.bz2'
    
    try:
        # Read input file and compress
        with open(input_file_path, 'rb') as input_file:
            data = input_file.read()
        
        # Compress data and write to output file
        with bz2.open(output_file_path, 'wb') as output_file:
            output_file.write(data)
        
        return output_file_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing {input_file_path}")
    except IOError as e:
        raise IOError(f"Error compressing file: {str(e)}")