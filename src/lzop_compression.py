import lzo
import struct

def lzop_compress(input_data):
    """
    Compress data using LZOP compression algorithm.
    
    Args:
        input_data (bytes): The input data to be compressed.
    
    Returns:
        bytes: Compressed data in LZOP format.
    
    Raises:
        ValueError: If input is not bytes or is empty.
        Exception: For any compression-related errors.
    """
    # Input validation
    if not isinstance(input_data, bytes):
        raise ValueError("Input must be bytes")
    
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    try:
        # Compress the data using python-lzo
        compressed_data = lzo.compress(input_data)
        
        # LZOP header structure:
        # - Magic number (4 bytes)
        # - Version (2 bytes)
        # - Compressed length (4 bytes)
        # - Uncompressed length (4 bytes)
        
        magic_number = b'LZOP'
        version = struct.pack('>H', 0x1030)  # LZOP version
        compressed_len = struct.pack('>I', len(compressed_data))
        uncompressed_len = struct.pack('>I', len(input_data))
        
        # Construct LZOP formatted output
        lzop_data = (
            magic_number + 
            version + 
            compressed_len + 
            uncompressed_len + 
            compressed_data
        )
        
        return lzop_data
    
    except Exception as e:
        raise Exception(f"LZOP compression failed: {str(e)}")

def lzop_decompress(lzop_data):
    """
    Decompress data compressed with LZOP algorithm.
    
    Args:
        lzop_data (bytes): Compressed data in LZOP format.
    
    Returns:
        bytes: Decompressed original data.
    
    Raises:
        ValueError: If input is not bytes, is empty, or has invalid format.
        Exception: For any decompression-related errors.
    """
    # Input validation
    if not isinstance(lzop_data, bytes):
        raise ValueError("Input must be bytes")
    
    if len(lzop_data) < 14:  # Minimum length for valid LZOP header
        raise ValueError("Invalid LZOP data: Too short")
    
    try:
        # Validate magic number
        if lzop_data[:4] != b'LZOP':
            raise ValueError("Invalid LZOP magic number")
        
        # Extract header information
        version = struct.unpack('>H', lzop_data[4:6])[0]
        compressed_len = struct.unpack('>I', lzop_data[6:10])[0]
        uncompressed_len = struct.unpack('>I', lzop_data[10:14])[0]
        
        # Extract compressed data
        compressed_data = lzop_data[14:]
        
        # Verify lengths
        if len(compressed_data) != compressed_len:
            raise ValueError("Compressed data length mismatch")
        
        # Decompress
        decompressed_data = lzo.decompress(compressed_data, uncompressed_len)
        
        return decompressed_data
    
    except Exception as e:
        raise Exception(f"LZOP decompression failed: {str(e)}")