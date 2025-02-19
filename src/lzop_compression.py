import lzo
import struct

def lzop_compress(data):
    """
    Compress data using the LZOP compression algorithm.
    
    Args:
        data (bytes): The input data to be compressed.
    
    Returns:
        bytes: Compressed data in LZOP format.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input data is empty.
    """
    # Input validation
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Compress data using python-lzo
    compressed_data = lzo.compress(data)
    
    # Create LZOP header (simplified version)
    # Header contains:
    # - Magic number (4 bytes)
    # - Version (2 bytes)
    # - Compressed length (4 bytes)
    # - Uncompressed length (4 bytes)
    magic_number = b'LZOP'
    version = struct.pack('>H', 0x1010)  # LZOP version 1.10
    compressed_len = struct.pack('>I', len(compressed_data))
    uncompressed_len = struct.pack('>I', len(data))
    
    # Combine header and compressed data
    lzop_data = magic_number + version + compressed_len + uncompressed_len + compressed_data
    
    return lzop_data

def lzop_decompress(lzop_data):
    """
    Decompress data compressed with the LZOP compression algorithm.
    
    Args:
        lzop_data (bytes): Compressed data in LZOP format.
    
    Returns:
        bytes: Decompressed original data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input data is invalid or incomplete.
    """
    # Input validation
    if not isinstance(lzop_data, bytes):
        raise TypeError("Input must be bytes")
    
    if len(lzop_data) < 16:  # Minimum header length
        raise ValueError("Invalid LZOP data: header too short")
    
    # Parse header
    magic_number = lzop_data[:4]
    if magic_number != b'LZOP':
        raise ValueError("Invalid LZOP magic number")
    
    # Extract compressed and uncompressed lengths
    compressed_len = struct.unpack('>I', lzop_data[8:12])[0]
    uncompressed_len = struct.unpack('>I', lzop_data[12:16])[0]
    
    # Extract compressed data
    compressed_data = lzop_data[16:16+compressed_len]
    
    # Decompress data
    decompressed_data = lzo.decompress(compressed_data, uncompressed_len)
    
    return decompressed_data