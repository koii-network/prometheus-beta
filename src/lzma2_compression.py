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
        ValueError: If input is empty.
    """
    # Validate input
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Convert str to bytes if necessary
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Validate input type
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compress using LZMA2 (LZMA with preset dictionary)
    try:
        # Use LZMA compression with LZMA2 preset
        compressed_data = lzma.compress(input_data, preset=9 | lzma.PRESET_EXTREME)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def lzma2_decompress(compressed_data):
    """
    Decompress data that was compressed using LZMA2 compression algorithm.
    
    Args:
        compressed_data (bytes): The data to be decompressed.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty.
        lzma.LZMAError: If decompression fails.
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    try:
        # Decompress using LZMA
        decompressed_data = lzma.decompress(compressed_data)
        return decompressed_data
    except lzma.LZMAError as e:
        raise lzma.LZMAError(f"Decompression failed: {str(e)}")