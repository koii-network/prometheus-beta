import bz2
import os

def decompress_bzip2_file(input_path, output_path=None):
    """
    Decompress a bzip2-compressed file.
    
    Args:
        input_path (str): Path to the bzip2-compressed input file.
        output_path (str, optional): Path to save the decompressed file. 
                                     If not provided, uses input filename without .bz2 extension.
    
    Returns:
        str: Path to the decompressed file.
    
    Raises:
        FileNotFoundError: If input file does not exist.
        ValueError: If input file is not a bzip2 compressed file.
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file {input_path} does not exist.")
    
    # Validate input is a bzip2 file
    if not input_path.endswith('.bz2'):
        raise ValueError(f"Input file {input_path} is not a .bz2 file.")
    
    # Determine output path if not provided
    if output_path is None:
        output_path = input_path.removesuffix('.bz2')
    
    # Decompress the file
    try:
        with bz2.open(input_path, 'rb') as source:
            with open(output_path, 'wb') as destination:
                destination.write(source.read())
    except Exception as e:
        raise ValueError(f"Error decompressing file: {e}")
    
    return output_path