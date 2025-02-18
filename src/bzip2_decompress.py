import bz2
import os

def decompress_bzip2_file(input_file_path, output_file_path=None):
    """
    Decompress a bzip2 compressed file.
    
    Args:
        input_file_path (str): Path to the bzip2 compressed input file.
        output_file_path (str, optional): Path to save the decompressed file. 
                                          If not provided, uses input filename without .bz2 extension.
    
    Returns:
        str: Path to the decompressed file.
    
    Raises:
        FileNotFoundError: If input file does not exist.
        PermissionError: If there are permission issues reading/writing files.
        ValueError: If input file is not a valid bzip2 compressed file.
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    # If no output path provided, create one by removing .bz2 extension
    if output_file_path is None:
        output_file_path = input_file_path.removesuffix('.bz2')
        if output_file_path == input_file_path:
            output_file_path += '.decompressed'
    
    try:
        # Open input and output files
        with bz2.open(input_file_path, 'rb') as compressed_file, \
             open(output_file_path, 'wb') as decompressed_file:
            # Read and decompress in chunks to handle large files
            decompressed_file.write(compressed_file.read())
        
        return output_file_path
    
    except bz2.BZip2Error:
        raise ValueError(f"Invalid bzip2 compressed file: {input_file_path}")