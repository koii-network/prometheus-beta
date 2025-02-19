import pytest
import lzo
import struct
from src.lzop_compression import compress_lzop

def test_compress_lzop_basic():
    """Test basic compression functionality"""
    original_data = b"Hello, world! This is a test of LZOP compression."
    compressed = compress_lzop(original_data)
    
    # Check that compressed data is different from original
    assert compressed != original_data
    assert len(compressed) < len(original_data)

def test_compress_lzop_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_lzop(b"")

def test_compress_lzop_invalid_input():
    """Test handling of non-bytes input"""
    with pytest.raises(TypeError, match="Input must be bytes"):
        compress_lzop("Not bytes")

def test_lzop_compression_decompression():
    """Test that compressed data can be decompressed correctly"""
    original_data = b"This is a more complex test of LZOP compression and decompression."
    
    # Compress
    compressed = compress_lzop(original_data)
    
    # Extract original size from header
    original_size = struct.unpack('>I', compressed[:4])[0]
    compressed_payload = compressed[4:]
    
    # Decompress
    decompressed = lzo.decompress(compressed_payload, original_size)
    
    # Verify
    assert decompressed == original_data
    assert len(decompressed) == original_size