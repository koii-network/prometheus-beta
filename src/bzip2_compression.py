import bz2
import os

def bzip2_compress(input_file_path, output_file_path=None):
    """
    Compress a file using Bzip2 compression algorithm.
    
    Args:
        input_file_path (str): Path to the input file to be compressed
        output_file_path (str, optional): Path to save the compressed file. 
                                          If not provided, appends '.bz2' to input file path.
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues reading/writing files
        IOError: For other I/O related errors
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # If no output path specified, create one by appending .bz2
    if output_file_path is None:
        output_file_path = input_file_path + '.bz2'
    
    try:
        # Read input file
        with open(input_file_path, 'rb') as input_file:
            data = input_file.read()
        
        # Compress data
        compressed_data = bz2.compress(data)
        
        # Write compressed data
        with open(output_file_path, 'wb') as output_file:
            output_file.write(compressed_data)
        
        return output_file_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_file_path} or {output_file_path}")
    except IOError as e:
        raise IOError(f"Error during compression: {str(e)}")

def bzip2_decompress(input_file_path, output_file_path=None):
    """
    Decompress a Bzip2 compressed file.
    
    Args:
        input_file_path (str): Path to the bzip2 compressed input file
        output_file_path (str, optional): Path to save the decompressed file. 
                                          If not provided, removes '.bz2' from input file path.
    
    Returns:
        str: Path to the decompressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues reading/writing files
        IOError: For other I/O related errors
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # If no output path specified, create one by removing .bz2
    if output_file_path is None:
        output_file_path = input_file_path.removesuffix('.bz2')
    
    try:
        # Read compressed input file
        with open(input_file_path, 'rb') as input_file:
            compressed_data = input_file.read()
        
        # Decompress data
        decompressed_data = bz2.decompress(compressed_data)
        
        # Write decompressed data
        with open(output_file_path, 'wb') as output_file:
            output_file.write(decompressed_data)
        
        return output_file_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_file_path} or {output_file_path}")
    except IOError as e:
        raise IOError(f"Error during decompression: {str(e)}")