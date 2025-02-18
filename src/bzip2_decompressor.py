import bz2
import os

def decompress_bzip2_file(compressed_file_path, output_file_path=None):
    """
    Decompress a bzip2-compressed file.

    Args:
        compressed_file_path (str): Path to the bzip2-compressed input file.
        output_file_path (str, optional): Path to save the decompressed file. 
                                          If not provided, uses input filename without .bz2 extension.

    Returns:
        str: Path to the decompressed file.

    Raises:
        FileNotFoundError: If the input compressed file does not exist.
        IsADirectoryError: If the input path is a directory.
        PermissionError: If there are permission issues reading/writing files.
    """
    # Validate input file
    if not os.path.exists(compressed_file_path):
        raise FileNotFoundError(f"Compressed file not found: {compressed_file_path}")
    
    if os.path.isdir(compressed_file_path):
        raise IsADirectoryError(f"Input path is a directory, not a file: {compressed_file_path}")

    # Determine output file path
    if output_file_path is None:
        # Remove .bz2 extension if present
        output_file_path = compressed_file_path.removesuffix('.bz2')
        if output_file_path == compressed_file_path:
            output_file_path += '.decompressed'

    # Decompress the file
    try:
        with bz2.open(compressed_file_path, 'rb') as compressed_file:
            with open(output_file_path, 'wb') as output_file:
                output_file.write(compressed_file.read())
    except PermissionError:
        raise PermissionError(f"Permission denied when reading {compressed_file_path} or writing {output_file_path}")

    return output_file_path