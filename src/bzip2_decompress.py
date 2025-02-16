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
    
    # Determine output file path if not provided
    if output_file_path is None:
        if not input_file_path.endswith('.bz2'):
            raise ValueError("Input file must have .bz2 extension if output path not specified")
        output_file_path = input_file_path[:-4]  # Remove .bz2 extension
    
    try:
        # Open and decompress the file
        with bz2.open(input_file_path, 'rb') as compressed_file:
            with open(output_file_path, 'wb') as decompressed_file:
                decompressed_file.write(compressed_file.read())
        
        return output_file_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_file_path} or {output_file_path}")
    except bz2.BZip2Error:
        raise ValueError(f"Invalid bzip2 compressed file: {input_file_path}")