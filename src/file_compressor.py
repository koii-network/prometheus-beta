import os
import bz2

def compress_file(input_path, output_path=None):
    """
    Compress a file using bzip2 compression.

    Args:
        input_path (str): Path to the input file to be compressed.
        output_path (str, optional): Path for the compressed output file. 
                                     If not provided, appends '.bz2' to input path.

    Returns:
        str: Path to the compressed file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are permission issues reading/writing files.
        IsADirectoryError: If input_path is a directory.
    """
    # Validate input file exists and is a file
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if os.path.isdir(input_path):
        raise IsADirectoryError(f"Input path is a directory, not a file: {input_path}")

    # Determine output path if not specified
    if output_path is None:
        output_path = input_path + '.bz2'

    try:
        # Open input file for reading
        with open(input_path, 'rb') as input_file:
            # Open output file for writing with bzip2 compression
            with bz2.open(output_path, 'wb') as output_file:
                # Read and compress in chunks to handle large files
                chunk = input_file.read(1024 * 1024)  # 1MB chunks
                while chunk:
                    output_file.write(chunk)
                    chunk = input_file.read(1024 * 1024)

        return output_path

    except PermissionError:
        raise PermissionError(f"Permission denied when accessing files: {input_path} or {output_path}")