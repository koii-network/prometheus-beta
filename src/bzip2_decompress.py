import bz2
import os

def decompress_bzip2_file(input_path, output_path=None):
    """
    Decompress a bzip2 compressed file.
    
    Args:
        input_path (str): Path to the input .bz2 compressed file
        output_path (str, optional): Path to save the decompressed file. 
                                     If not provided, uses input filename without .bz2 extension
    
    Returns:
        str: Path to the decompressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If there are permission issues
        IsADirectoryError: If input path is a directory
        bz2.BZ2Error: If there are issues with bzip2 decompression
    """
    # Validate input path
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if os.path.isdir(input_path):
        raise IsADirectoryError(f"Input path is a directory, not a file: {input_path}")
    
    # Determine output path if not provided
    if output_path is None:
        # Remove .bz2 extension if present
        output_path = input_path.removesuffix('.bz2') if input_path.endswith('.bz2') else input_path + '_decompressed'
    
    try:
        # Decompress the file
        with bz2.open(input_path, 'rb') as source_file:
            with open(output_path, 'wb') as dest_file:
                dest_file.write(source_file.read())
        
        return output_path
    
    except PermissionError:
        raise PermissionError(f"Permission denied when trying to decompress {input_path}")
    except bz2.BZ2Error as e:
        raise bz2.BZ2Error(f"Error decompressing bzip2 file: {e}")