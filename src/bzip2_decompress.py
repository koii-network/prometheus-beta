import bz2
import os

def decompress_bzip2_file(input_file_path, output_file_path=None):
    """
    Decompress a bzip2-compressed file.
    
    Args:
        input_file_path (str): Path to the bzip2-compressed input file
        output_file_path (str, optional): Path to save the decompressed file. 
                                          If not provided, uses input filename without .bz2 extension
    
    Returns:
        str: Path to the decompressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        IOError: If there are issues reading or writing files
        ValueError: If input file is not a valid bzip2 compressed file
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # Determine output file path
    if output_file_path is None:
        # Remove .bz2 extension if present
        output_file_path = input_file_path.removesuffix('.bz2') if input_file_path.endswith('.bz2') else input_file_path + '_decompressed'
    
    try:
        # Decompress the file
        with bz2.open(input_file_path, 'rb') as compressed_file:
            with open(output_file_path, 'wb') as output_file:
                output_file.write(compressed_file.read())
        
        return output_file_path
    
    except bz2.BZ2Error as e:
        raise ValueError(f"Invalid bzip2 compressed file: {e}")
    except IOError as e:
        raise IOError(f"Error reading or writing files: {e}")