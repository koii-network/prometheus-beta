import zstandard as zstd
import os
from typing import Union, BinaryIO


def compress_data(data: Union[bytes, str], compression_level: int = 3) -> bytes:
    """
    Compress data using Zstandard compression algorithm.

    Args:
        data (Union[bytes, str]): The data to compress. 
            If str is provided, it will be encoded to bytes.
        compression_level (int, optional): Compression level from 1-22. 
            Defaults to 3. Higher levels provide better compression 
            but take more time.

    Returns:
        bytes: Compressed data

    Raises:
        TypeError: If input is not bytes or str
        ValueError: If compression level is out of valid range
    """
    # Validate input type
    if isinstance(data, str):
        data = data.encode('utf-8')
    elif not isinstance(data, bytes):
        raise TypeError("Input must be bytes or string")

    # Validate compression level
    if not (1 <= compression_level <= 22):
        raise ValueError("Compression level must be between 1 and 22")

    # Create compressor
    cctx = zstd.ZstdCompressor(level=compression_level)
    
    # Compress the data
    return cctx.compress(data)


def decompress_data(compressed_data: bytes) -> bytes:
    """
    Decompress Zstandard compressed data.

    Args:
        compressed_data (bytes): The data to decompress

    Returns:
        bytes: Decompressed data

    Raises:
        TypeError: If input is not bytes
        zstd.ZstdError: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")

    # Create decompressor
    dctx = zstd.ZstdDecompressor()
    
    # Decompress the data
    return dctx.decompress(compressed_data)


def compress_file(input_path: str, output_path: str = None, 
                  compression_level: int = 3) -> str:
    """
    Compress a file using Zstandard compression.

    Args:
        input_path (str): Path to the input file
        output_path (str, optional): Path to save compressed file. 
            If None, appends '.zst' to input path
        compression_level (int, optional): Compression level. 
            Defaults to 3.

    Returns:
        str: Path to the compressed file

    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If file cannot be read or written
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Determine output path
    if output_path is None:
        output_path = input_path + '.zst'

    # Open input and output files
    with open(input_path, 'rb') as input_file, \
         open(output_path, 'wb') as output_file:
        # Create compressor
        cctx = zstd.ZstdCompressor(level=compression_level)
        
        # Compress file
        with cctx.stream_writer(output_file) as compressor:
            # Read and compress in chunks to handle large files
            for chunk in iter(lambda: input_file.read(64 * 1024), b''):
                compressor.write(chunk)

    return output_path


def decompress_file(input_path: str, output_path: str = None) -> str:
    """
    Decompress a Zstandard compressed file.

    Args:
        input_path (str): Path to the compressed input file
        output_path (str, optional): Path to save decompressed file. 
            If None, removes '.zst' extension if present

    Returns:
        str: Path to the decompressed file

    Raises:
        FileNotFoundError: If input file does not exist
        ValueError: If input file does not have .zst extension
        PermissionError: If file cannot be read or written
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Determine output path
    if output_path is None:
        if not input_path.endswith('.zst'):
            raise ValueError("Input file must have .zst extension")
        output_path = input_path[:-4]  # Remove .zst extension

    # Open input and output files
    with open(input_path, 'rb') as input_file, \
         open(output_path, 'wb') as output_file:
        # Create decompressor
        dctx = zstd.ZstdDecompressor()
        
        # Decompress file
        with dctx.stream_reader(input_file) as decompressor:
            # Read and decompress in chunks to handle large files
            for chunk in iter(lambda: decompressor.read(64 * 1024), b''):
                output_file.write(chunk)

    return output_path