import lzo
import typing

def compress_lzo(data: typing.Union[bytes, str]) -> bytes:
    """
    Compress data using Lempel-Ziv-Oberhumer (LZO) compression algorithm.
    
    Args:
        data (Union[bytes, str]): The input data to compress. 
                                   If str is provided, it will be encoded to bytes.
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input data is empty
    """
    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Compress using LZO
    try:
        compressed_data = lzo.compress(data)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"LZO compression failed: {str(e)}")

def decompress_lzo(compressed_data: bytes) -> bytes:
    """
    Decompress data using Lempel-Ziv-Oberhumer (LZO) compression algorithm.
    
    Args:
        compressed_data (bytes): The compressed data to decompress
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input data is empty
        RuntimeError: If decompression fails
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    # Decompress using LZO
    try:
        decompressed_data = lzo.decompress(compressed_data)
        return decompressed_data
    except Exception as e:
        raise RuntimeError(f"LZO decompression failed: {str(e)}")