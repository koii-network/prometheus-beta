import lzma
import io

def lzma2_compress(input_data):
    """
    Compress input data using LZMA2 compression algorithm.
    
    Args:
        input_data (bytes or str): The data to be compressed.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Validate input
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Convert string to bytes if necessary
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    
    # Ensure input is bytes
    if not isinstance(input_data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compress using LZMA2 (LZMA with improved compression)
    try:
        # Use LZMA compression with LZMA2 preset
        compressed = lzma.compress(input_data, preset=lzma.PRESET_EXTREME)
        return compressed
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def lzma2_decompress(compressed_data):
    """
    Decompress data compressed with LZMA2 algorithm.
    
    Args:
        compressed_data (bytes): The compressed data to decompress.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty.
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    try:
        # Decompress using LZMA
        decompressed = lzma.decompress(compressed_data)
        return decompressed
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")