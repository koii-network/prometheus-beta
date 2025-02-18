import lzma
import os
from typing import Union, Optional

def compress_xz(input_path: str, output_path: Optional[str] = None, compression_level: int = 6) -> str:
    """
    Compress a file or data using XZ compression.

    Args:
        input_path (str): Path to the input file to be compressed.
        output_path (Optional[str], optional): Path to save the compressed file. 
            If not provided, appends '.xz' to the input path.
        compression_level (int, optional): Compression level from 0-9. 
            Defaults to 6 (balanced between compression ratio and speed).

    Returns:
        str: Path to the compressed file.

    Raises:
        FileNotFoundError: If input file does not exist.
        ValueError: If compression level is out of valid range.
    """
    # Validate compression level
    if compression_level < 0 or compression_level > 9:
        raise ValueError("Compression level must be between 0 and 9")

    # Check if input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Determine output path if not specified
    if output_path is None:
        output_path = input_path + '.xz'

    # Perform XZ compression
    with open(input_path, 'rb') as input_file, \
         lzma.open(output_path, 'wb', preset=compression_level) as compressed_file:
        compressed_file.write(input_file.read())

    return output_path

def decompress_xz(input_path: str, output_path: Optional[str] = None) -> str:
    """
    Decompress an XZ compressed file.

    Args:
        input_path (str): Path to the XZ compressed input file.
        output_path (Optional[str], optional): Path to save the decompressed file. 
            If not provided, removes '.xz' from the input path.

    Returns:
        str: Path to the decompressed file.

    Raises:
        FileNotFoundError: If input file does not exist.
        ValueError: If input file is not an XZ compressed file.
    """
    # Check if input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Determine output path if not specified
    if output_path is None:
        if not input_path.endswith('.xz'):
            raise ValueError("Input file must have .xz extension if no output path is provided")
        output_path = input_path[:-3]  # Remove .xz extension

    # Perform XZ decompression
    with lzma.open(input_path, 'rb') as compressed_file, \
         open(output_path, 'wb') as output_file:
        output_file.write(compressed_file.read())

    return output_path