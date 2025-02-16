import lzma
import io

def lzma2_compress(input_data):
    """
    Compress data using LZMA2 compression algorithm.
    
    Args:
        input_data (bytes or str): The data to be compressed.
    
    Returns:
        bytes: Compressed data using LZMA2 compression.
    
    Raises:
        TypeError: If input is not bytes or str.
    """
    # Convert input to bytes if it's a string
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Validate input type
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compress using LZMA2 (LZMA with newer preset parameters)
    compressed_data = lzma.compress(input_data, preset=9 | lzma.PRESET_EXTREME)
    
    return compressed_data

def lzma2_decompress(compressed_data):
    """
    Decompress data that was compressed with LZMA2.
    
    Args:
        compressed_data (bytes): The data to be decompressed.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        lzma.LZMAError: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress using LZMA2
    decompressed_data = lzma.decompress(compressed_data)
    
    return decompressed_data