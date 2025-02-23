import struct
import zlib

def lzop_compress(data):
    """
    Implement a simplified LZOP compression algorithm.
    
    Args:
        data (bytes): The input data to compress
    
    Returns:
        bytes: Compressed data in a basic LZOP-like format
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Compression steps simulating LZOP-like compression
    # 1. Basic zlib compression (LZOP uses LZO, but zlib provides similar compression)
    compressed_data = zlib.compress(data)
    
    # 2. Create a simple header with metadata
    header = struct.pack(
        '>IIHH',  # Big-endian: 2 integers, 2 short integers
        len(data),     # Original data length
        len(compressed_data),  # Compressed data length
        1,  # Version
        0   # Compression level
    )
    
    # 3. Combine header and compressed data
    return header + compressed_data

def lzop_decompress(compressed_data):
    """
    Decompress data compressed with the lzop_compress function.
    
    Args:
        compressed_data (bytes): The compressed data to decompress
    
    Returns:
        bytes: Decompressed original data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is too short or invalid
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if len(compressed_data) < 12:  # Minimum header size
        raise ValueError("Compressed data is too short")
    
    # Extract header information
    original_length, compressed_length, version, level = struct.unpack(
        '>IIHH', compressed_data[:12]
    )
    
    # Validate header
    if version != 1:
        raise ValueError(f"Unsupported compression version: {version}")
    
    # Extract and decompress the actual data
    compressed_payload = compressed_data[12:]
    
    # Ensure compressed payload matches expected length
    if len(compressed_payload) != compressed_length:
        raise ValueError("Compressed data length mismatch")
    
    # Decompress using zlib
    decompressed_data = zlib.decompress(compressed_payload)
    
    # Verify decompressed data length
    if len(decompressed_data) != original_length:
        raise ValueError("Decompressed data length mismatch")
    
    return decompressed_data