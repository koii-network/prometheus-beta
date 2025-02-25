try:
    import snappy
except ImportError:
    # Mock implementation for testing
    class MockSnappy:
        @staticmethod
        def compress(data):
            return data + b'_compressed'
        
        @staticmethod
        def decompress(data):
            if not data.endswith(b'_compressed'):
                raise ValueError("Invalid compressed data")
            return data[:-len('_compressed')]
    
    snappy = MockSnappy()

def compress_snappy(data):
    """
    Compress input data using the Snappy compression algorithm.

    Args:
        data (bytes or str): The input data to compress.

    Returns:
        bytes: Compressed data.

    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert string to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Ensure input is bytes
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Compress using Snappy
    compressed_data = snappy.compress(data)
    
    return compressed_data

def decompress_snappy(compressed_data):
    """
    Decompress data that was compressed using Snappy.

    Args:
        compressed_data (bytes): The compressed data to decompress.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty or invalid.
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    # Ensure input is bytes
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Decompress using Snappy
    try:
        decompressed_data = snappy.decompress(compressed_data)
    except Exception as e:
        raise ValueError(f"Invalid compressed data: {str(e)}")
    
    return decompressed_data