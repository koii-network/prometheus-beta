import gzip
import io

def compress_data(data):
    """
    Compress input data using Gzip compression.
    
    Args:
        data (str or bytes): The data to be compressed.
    
    Returns:
        bytes: Compressed data in Gzip format.
    
    Raises:
        TypeError: If input is not a string or bytes.
        ValueError: If input is empty.
    """
    # Validate input
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be a string or bytes")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert string to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Compress data
    with io.BytesIO() as bio:
        with gzip.GzipFile(fileobj=bio, mode='wb') as gzipfile:
            gzipfile.write(data)
        compressed_data = bio.getvalue()
    
    return compressed_data

def decompress_data(compressed_data):
    """
    Decompress Gzip compressed data.
    
    Args:
        compressed_data (bytes): Gzip compressed data.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty or invalid Gzip data.
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    # Decompress data
    try:
        with gzip.GzipFile(fileobj=io.BytesIO(compressed_data), mode='rb') as gzipfile:
            decompressed_data = gzipfile.read()
    except (IOError, gzip.BadGzipFile) as e:
        raise ValueError(f"Invalid Gzip data: {str(e)}")
    
    return decompressed_data