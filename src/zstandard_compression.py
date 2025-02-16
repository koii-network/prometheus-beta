import zstandard as zstd
import os

def compress_file(input_path, output_path=None, compression_level=3):
    """
    Compress a file using Zstandard compression algorithm.
    
    Args:
        input_path (str): Path to the input file to be compressed
        output_path (str, optional): Path to save the compressed file. 
                                     If not provided, appends '.zst' to input path
        compression_level (int, optional): Compression level (1-22). 
                                           Defaults to 3 (balanced compression/speed)
    
    Returns:
        str: Path to the compressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        ValueError: If compression level is out of valid range
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Validate compression level
    if compression_level < 1 or compression_level > 22:
        raise ValueError("Compression level must be between 1 and 22")
    
    # Determine output path
    if output_path is None:
        output_path = input_path + '.zst'
    
    # Create Zstandard compressor
    cctx = zstd.ZstdCompressor(level=compression_level)
    
    # Perform compression
    with open(input_path, 'rb') as input_file, \
         open(output_path, 'wb') as output_file:
        cctx.copy_stream(input_file, output_file)
    
    return output_path

def decompress_file(input_path, output_path=None):
    """
    Decompress a Zstandard compressed file.
    
    Args:
        input_path (str): Path to the Zstandard compressed file
        output_path (str, optional): Path to save the decompressed file. 
                                     If not provided, removes '.zst' from input path
    
    Returns:
        str: Path to the decompressed file
    
    Raises:
        FileNotFoundError: If input file does not exist
        ValueError: If input file does not have .zst extension
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Validate input file extension
    if not input_path.endswith('.zst'):
        raise ValueError("Input file must have .zst extension")
    
    # Determine output path
    if output_path is None:
        output_path = input_path[:-4]  # Remove .zst extension
    
    # Create Zstandard decompressor
    dctx = zstd.ZstdDecompressor()
    
    # Perform decompression
    with open(input_path, 'rb') as input_file, \
         open(output_path, 'wb') as output_file:
        dctx.copy_stream(input_file, output_file)
    
    return output_path