import lzo
import struct
import io

def lzop_compress(input_data):
    """
    Implement LZOP compression algorithm.
    
    Args:
        input_data (bytes): The input data to compress
    
    Returns:
        bytes: Compressed data in LZOP format
    
    Raises:
        ValueError: If input is not bytes
        RuntimeError: If compression fails
    """
    # Validate input
    if not isinstance(input_data, bytes):
        raise ValueError("Input must be bytes")
    
    if not input_data:
        return b''
    
    try:
        # Compress the data using python-lzo
        compressed_data = lzo.compress(input_data)
        
        # Create LZOP header (simplified version)
        header = b'\x4c\x5a\x4f\x50'  # Magic number
        header += struct.pack('>I', len(input_data))  # Uncompressed size
        header += struct.pack('>I', len(compressed_data))  # Compressed size
        
        # Combine header and compressed data
        return header + compressed_data
    
    except Exception as e:
        raise RuntimeError(f"LZOP compression failed: {str(e)}")