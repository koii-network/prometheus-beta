import os
import bz2

def decompress_bzip2_file(compressed_filepath, output_filepath=None):
    """
    Decompress a bzip2-compressed file.

    Args:
        compressed_filepath (str): Path to the bzip2-compressed input file.
        output_filepath (str, optional): Path to save the decompressed file. 
                                         If not provided, uses input filename without .bz2 extension.

    Returns:
        str: Path to the decompressed file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        IsADirectoryError: If the input filepath is a directory.
        PermissionError: If there are insufficient permissions to read/write files.
        ValueError: If the input filepath is not a bzip2 compressed file.
    """
    # Validate input file
    if not os.path.exists(compressed_filepath):
        raise FileNotFoundError(f"Compressed file not found: {compressed_filepath}")
    
    if os.path.isdir(compressed_filepath):
        raise IsADirectoryError(f"Input path is a directory, not a file: {compressed_filepath}")
    
    # Validate bz2 extension
    if not compressed_filepath.endswith('.bz2'):
        raise ValueError(f"File must have .bz2 extension: {compressed_filepath}")

    # Determine output filepath
    if output_filepath is None:
        output_filepath = compressed_filepath.rstrip('.bz2')

    try:
        # Open and decompress the file
        with bz2.open(compressed_filepath, 'rb') as compressed_file:
            decompressed_content = compressed_file.read()
        
        # Write decompressed content to output file
        with open(output_filepath, 'wb') as output_file:
            output_file.write(decompressed_content)
        
        return output_filepath

    except PermissionError:
        raise PermissionError(f"Unable to read compressed file or write output file: {compressed_filepath}")
    except (OSError, EOFError):
        raise ValueError(f"Invalid or corrupted bzip2 compressed file: {compressed_filepath}")