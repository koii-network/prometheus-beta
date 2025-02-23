import os
import bz2

def compress_file(input_path, output_path=None):
    """
    Compress a file using bzip2 compression.

    Args:
        input_path (str): Path to the input file to be compressed.
        output_path (str, optional): Path to save the compressed file. 
                                     If not provided, appends '.bz2' to input path.

    Returns:
        str: Path to the compressed file.

    Raises:
        FileNotFoundError: If input file does not exist.
        PermissionError: If there are permission issues reading/writing files.
        IsADirectoryError: If input path is a directory instead of a file.
    """
    # Validate input file exists and is a file
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if not os.path.isfile(input_path):
        raise IsADirectoryError(f"Input path must be a file, not a directory: {input_path}")

    # Determine output path if not provided
    if output_path is None:
        output_path = input_path + '.bz2'

    try:
        # Read input file
        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()

        # Compress data
        compressed_data = bz2.compress(input_data)

        # Write compressed data
        with open(output_path, 'wb') as output_file:
            output_file.write(compressed_data)

        return output_path

    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_path}, {output_path}")