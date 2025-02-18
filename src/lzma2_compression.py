import lzma
import io

def compress_lzma2(input_data, preset=6):
    """
    Compress data using LZMA2 compression algorithm.
    
    Args:
        input_data (bytes or str): Data to be compressed
        preset (int, optional): Compression level (0-9). Defaults to 6.
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If preset is not between 0 and 9
    """
    # Validate input type
    if not isinstance(input_data, (bytes, str)):
        raise TypeError("Input must be bytes or str")
    
    # Validate preset range
    if not 0 <= preset <= 9:
        raise ValueError("Preset must be between 0 and 9")
    
    # Convert str to bytes if necessary
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Compress using LZMA2 (LZMA format)
    compressed = lzma.compress(input_data, preset=preset | lzma.PRESET_EXTREME)
    
    return compressed

def decompress_lzma2(compressed_data):
    """
    Decompress data compressed with LZMA2 compression algorithm.
    
    Args:
        compressed_data (bytes): Compressed data to decompress
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        lzma.LZMAError: If decompression fails
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress using LZMA2
    decompressed = lzma.decompress(compressed_data)
    
    return decompressed