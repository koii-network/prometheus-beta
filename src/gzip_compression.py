import gzip
import os

def compress_file(input_file, output_file=None):
    """
    Compress a file using Gzip compression.
    
    Args:
        input_file (str): Path to the input file to be compressed
        output_file (str, optional): Path for the compressed output file. 
                                     If not provided, appends '.gz' to input filename.
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues
        IOError: For other IO-related errors
    """
    # Validate input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist")
    
    # If no output file specified, create default by appending .gz
    if output_file is None:
        output_file = input_file + '.gz'
    
    try:
        # Open input file in binary read mode
        with open(input_file, 'rb') as f_in:
            # Open gzip compressed file in write mode
            with gzip.open(output_file, 'wb') as f_out:
                # Copy contents, compressing as it goes
                f_out.writelines(f_in)
        
        return output_file
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing {input_file} or {output_file}")
    except IOError as e:
        raise IOError(f"Error during compression: {e}")

def decompress_file(input_file, output_file=None):
    """
    Decompress a Gzip compressed file.
    
    Args:
        input_file (str): Path to the Gzip compressed input file
        output_file (str, optional): Path for the decompressed output file.
                                     If not provided, removes '.gz' from input filename.
    
    Returns:
        str: Path to the decompressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues
        IOError: For other IO-related errors
    """
    # Validate input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist")
    
    # If no output file specified, create default by removing .gz
    if output_file is None:
        output_file = input_file.removesuffix('.gz')
    
    try:
        # Open gzip compressed file in read mode
        with gzip.open(input_file, 'rb') as f_in:
            # Open decompressed file in write mode
            with open(output_file, 'wb') as f_out:
                # Copy contents, decompressing as it goes
                f_out.writelines(f_in)
        
        return output_file
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing {input_file} or {output_file}")
    except IOError as e:
        raise IOError(f"Error during decompression: {e}")