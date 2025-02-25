import zstandard as zstd
import os

def compress_file(input_path, output_path=None, compression_level=3):
    """
    Compress a file using Zstandard compression algorithm.
    
    Args:
        input_path (str): Path to the input file to be compressed.
        output_path (str, optional): Path for the compressed output file. 
                                     If not provided, appends '.zst' to input path.
        compression_level (int, optional): Compression level from 1-22. 
                                           Default is 3 (balanced speed and compression).
    
    Returns:
        str: Path to the compressed output file.
    
    Raises:
        FileNotFoundError: If input file does not exist.
        ValueError: If compression level is out of valid range.
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
    
    # Compress the file
    with open(input_path, 'rb') as input_file, \
         open(output_path, 'wb') as output_file:
        cctx.copy_stream(input_file, output_file)
    
    return output_path

def decompress_file(input_path, output_path=None):
    """
    Decompress a Zstandard compressed file.
    
    Args:
        input_path (str): Path to the Zstandard compressed input file.
        output_path (str, optional): Path for the decompressed output file.
                                     If not provided, removes '.zst' extension.
    
    Returns:
        str: Path to the decompressed output file.
    
    Raises:
        FileNotFoundError: If input file does not exist.
        ValueError: If input file does not have .zst extension.
    """
    # Validate input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Validate input is a .zst file
    if not input_path.endswith('.zst'):
        raise ValueError("Input file must have .zst extension")
    
    # Determine output path
    if output_path is None:
        output_path = input_path[:-4]  # Remove .zst extension
    
    # Create Zstandard decompressor
    dctx = zstd.ZstdDecompressor()
    
    # Decompress the file
    with open(input_path, 'rb') as input_file, \
         open(output_path, 'wb') as output_file:
        dctx.copy_stream(input_file, output_file)
    
    return output_path