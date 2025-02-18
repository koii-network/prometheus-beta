import zstandard as zstd

def compress_data(input_data, compression_level=3):
    """
    Compress input data using Zstandard compression algorithm.
    
    Args:
        input_data (bytes or str): Data to be compressed.
        compression_level (int, optional): Compression level from 1-22. Defaults to 3.
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If compression level is out of valid range
    """
    # Convert str to bytes if necessary
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Validate input type
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Validate compression level
    if not 1 <= compression_level <= 22:
        raise ValueError("Compression level must be between 1 and 22")
    
    # Create compressor
    cctx = zstd.ZstdCompressor(level=compression_level)
    
    # Compress data
    compressed_data = cctx.compress(input_data)
    
    return compressed_data

def decompress_data(compressed_data):
    """
    Decompress Zstandard compressed data.
    
    Args:
        compressed_data (bytes): Zstandard compressed data
    
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
    
    # Decompress data
    decompressed_data = dctx.decompress(compressed_data)
    
    return decompressed_data