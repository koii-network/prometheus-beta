import lzo
import io

def lzo_compress(data):
    """
    Compress input data using LZO compression algorithm.
    
    Args:
        data (bytes or str): The input data to compress. 
                              If str, it will be encoded to bytes first.
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input is empty
    """
    # Validate input
    if data is None:
        raise ValueError("Input data cannot be None")
    
    # Convert str to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Check for empty input
    if len(data) == 0:
        raise ValueError("Input data cannot be empty")
    
    # Compress the data
    try:
        compressed_data = lzo.compress(data)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def lzo_decompress(compressed_data):
    """
    Decompress LZO compressed data.
    
    Args:
        compressed_data (bytes): The LZO compressed data to decompress
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty
        RuntimeError: If decompression fails
    """
    # Validate input
    if compressed_data is None:
        raise ValueError("Compressed data cannot be None")
    
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Check for empty input
    if len(compressed_data) == 0:
        raise ValueError("Compressed data cannot be empty")
    
    # Decompress the data
    try:
        decompressed_data = lzo.decompress(compressed_data)
        return decompressed_data
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")