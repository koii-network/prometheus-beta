import lzo
import struct
import zlib

def lzop_compress(data):
    """
    Implement LZOP compression algorithm.
    
    Args:
        data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data in LZOP format
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If compression fails
    """
    # Input validation
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        return b''
    
    try:
        # Compress data using LZO
        compressed_data = lzo.compress(data, lzo.LZO_COMPRESSION_LEVEL_DEFAULT)
        
        # Create LZOP header
        # Magic number for LZOP
        magic_number = b'\x4c\x5a\x4f\x50'
        
        # Version (1.08)
        version = struct.pack('>H', 0x1008)
        
        # Compression library (LZO1X)
        library_version = struct.pack('>H', 0x1010)
        
        # Compressed and uncompressed sizes
        uncompressed_size = struct.pack('<Q', len(data))
        compressed_size = struct.pack('<Q', len(compressed_data))
        
        # Checksum (using Adler-32)
        adler32_checksum = struct.pack('<I', zlib.adler32(data) & 0xFFFFFFFF)
        
        # Combine all components
        lzop_compressed = (
            magic_number +
            version +
            library_version +
            uncompressed_size +
            compressed_size +
            adler32_checksum +
            compressed_data
        )
        
        return lzop_compressed
    
    except Exception as e:
        raise ValueError(f"Compression failed: {str(e)}")

def lzop_decompress(compressed_data):
    """
    Implement LZOP decompression algorithm.
    
    Args:
        compressed_data (bytes): LZOP compressed data
    
    Returns:
        bytes: Decompressed original data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If decompression fails or data is invalid
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        return b''
    
    try:
        # Validate magic number
        if compressed_data[:4] != b'\x4c\x5a\x4f\x50':
            raise ValueError("Invalid LZOP magic number")
        
        # Parse header
        version = struct.unpack('>H', compressed_data[4:6])[0]
        library_version = struct.unpack('>H', compressed_data[6:8])[0]
        
        # Extract sizes and checksum
        uncompressed_size = struct.unpack('<Q', compressed_data[8:16])[0]
        compressed_size = struct.unpack('<Q', compressed_data[16:24])[0]
        original_checksum = struct.unpack('<I', compressed_data[24:28])[0]
        
        # Extract compressed data
        compressed_payload = compressed_data[28:]
        
        # Decompress using LZO
        decompressed_data = lzo.decompress(compressed_payload, uncompressed_size)
        
        # Verify checksum
        calculated_checksum = zlib.adler32(decompressed_data) & 0xFFFFFFFF
        if calculated_checksum != original_checksum:
            raise ValueError("Checksum verification failed")
        
        return decompressed_data
    
    except Exception as e:
        raise ValueError(f"Decompression failed: {str(e)}")