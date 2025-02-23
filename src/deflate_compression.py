import zlib

def deflate_compress(data):
    """
    Implement Deflate compression algorithm using zlib.

    Args:
        data (bytes or str): The input data to compress.
        
    Returns:
        bytes: Compressed data using Deflate compression.
        
    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Ensure input is bytes
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compress using zlib (which implements Deflate)
    # wbits=-15 specifies raw Deflate encoding without zlib or gzip headers
    try:
        compressed_data = zlib.compress(data, level=zlib.Z_DEFAULT_COMPRESSION)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def deflate_decompress(compressed_data):
    """
    Decompress data using Deflate algorithm.

    Args:
        compressed_data (bytes): The compressed input data.
        
    Returns:
        bytes: Decompressed data.
        
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty.
        RuntimeError: If decompression fails.
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Decompress using zlib (which implements Deflate)
    # wbits=-15 specifies raw Deflate decoding without zlib or gzip headers
    try:
        decompressed_data = zlib.decompress(compressed_data, wbits=-15)
        return decompressed_data
    except Exception as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")