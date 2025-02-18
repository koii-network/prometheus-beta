import bz2
import os

def compress_file_bzip2(input_file, output_file=None):
    """
    Compress a file using bzip2 compression.

    Args:
        input_file (str): Path to the input file to be compressed.
        output_file (str, optional): Path for the compressed output file. 
                                     If not provided, appends '.bz2' to input filename.

    Returns:
        str: Path to the compressed file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are permission issues reading/writing files.
    """
    # Validate input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file {input_file} does not exist.")

    # If no output file specified, create one by appending .bz2
    if output_file is None:
        output_file = input_file + '.bz2'

    try:
        # Read input file
        with open(input_file, 'rb') as f_input:
            input_data = f_input.read()

        # Compress data
        compressed_data = bz2.compress(input_data)

        # Write compressed data
        with open(output_file, 'wb') as f_output:
            f_output.write(compressed_data)

        return output_file

    except PermissionError:
        raise PermissionError(f"Permission denied when accessing {input_file} or {output_file}")