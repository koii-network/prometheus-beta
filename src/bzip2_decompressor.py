import bz2
import os

def decompress_bzip2_file(input_file_path, output_file_path=None):
    """
    Decompress a bzip2 compressed file.

    Args:
        input_file_path (str): Path to the input bzip2 compressed file.
        output_file_path (str, optional): Path to save the decompressed file. 
                                          If not provided, uses input filename without .bz2 extension.

    Returns:
        str: Path to the decompressed file.

    Raises:
        FileNotFoundError: If input file does not exist.
        IOError: If there are issues with file reading/writing.
    """
    # Validate input file exists
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file {input_file_path} does not exist.")

    # Determine output file path
    if output_file_path is None:
        # Remove .bz2 extension if present
        output_file_path = input_file_path.removesuffix('.bz2') if input_file_path.endswith('.bz2') else input_file_path + '_decompressed'

    try:
        # Open input and output files
        with bz2.open(input_file_path, 'rb') as compressed_file, \
             open(output_file_path, 'wb') as decompressed_file:
            # Read and decompress the file in chunks
            decompressed_file.write(compressed_file.read())

        return output_file_path

    except IOError as e:
        raise IOError(f"Error during decompression: {e}")