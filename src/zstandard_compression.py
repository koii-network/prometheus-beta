import zstandard as zstd
import io
from typing import Union, BinaryIO


def compress_data(data: Union[bytes, str], compression_level: int = 3) -> bytes:
    """
    Compress data using Zstandard compression algorithm.

    Args:
        data (Union[bytes, str]): The data to compress. 
                                   If str, it will be encoded to UTF-8 bytes.
        compression_level (int, optional): Compression level from 1-22. 
                                           Defaults to 3 (balanced speed/compression).

    Returns:
        bytes: Compressed data

    Raises:
        TypeError: If input is not bytes or str
        ValueError: If compression level is out of valid range
    """
    # Validate input type
    if not isinstance(data, (bytes, str)):
        raise TypeError("Input must be bytes or str")
    
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate compression level
    if not 1 <= compression_level <= 22:
        raise ValueError("Compression level must be between 1 and 22")

    # Create compressor
    cctx = zstd.ZstdCompressor(level=compression_level)
    
    # Compress and return
    return cctx.compress(data)


def decompress_data(compressed_data: bytes) -> bytes:
    """
    Decompress Zstandard compressed data.

    Args:
        compressed_data (bytes): Zstandard compressed data to decompress

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
    
    # Decompress and return
    return dctx.decompress(compressed_data)


def compress_file(input_path: str, output_path: str = None, 
                  compression_level: int = 3) -> str:
    """
    Compress a file using Zstandard compression.

    Args:
        input_path (str): Path to the input file to compress
        output_path (str, optional): Path to save compressed file. 
                                     If None, appends '.zst' to input path.
        compression_level (int, optional): Compression level from 1-22. 
                                           Defaults to 3.

    Returns:
        str: Path to the compressed file

    Raises:
        FileNotFoundError: If input file does not exist
        ValueError: If compression level is out of valid range
    """
    # Validate compression level
    if not 1 <= compression_level <= 22:
        raise ValueError("Compression level must be between 1 and 22")

    # Determine output path
    if output_path is None:
        output_path = input_path + '.zst'

    # Create compressor
    cctx = zstd.ZstdCompressor(level=compression_level)

    # Compress file
    with open(input_path, 'rb') as input_file, \
         open(output_path, 'wb') as output_file:
        cctx.copy_stream(input_file, output_file)

    return output_path