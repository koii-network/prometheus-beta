import pytest
import lzo
import struct
from src.lzop_compression import lzop_compress

def test_lzop_compress_basic():
    """Test basic compression functionality"""
    test_data = b"Hello, this is a test string for LZOP compression!"
    compressed = lzop_compress(test_data)
    
    # Check that compressed data is longer than header
    assert len(compressed) > 4
    
    # Check header contains original length
    original_length = struct.unpack('>I', compressed[:4])[0]
    assert original_length == len(test_data)
    
    # Verify decompression works
    decompressed = lzo.decompress(compressed[4:], False, original_length)
    assert decompressed == test_data

def test_lzop_compress_empty_input():
    """Test compression with empty input raises ValueError"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzop_compress(b"")

def test_lzop_compress_invalid_type():
    """Test compression with invalid input type raises TypeError"""
    with pytest.raises(TypeError, match="Input must be bytes"):
        lzop_compress("Not bytes")

def test_lzop_compress_large_data():
    """Test compression with larger data"""
    test_data = b"A" * 10000
    compressed = lzop_compress(test_data)
    
    # Check that compressed data is longer than header
    assert len(compressed) > 4
    
    # Check header contains original length
    original_length = struct.unpack('>I', compressed[:4])[0]
    assert original_length == len(test_data)
    
    # Verify decompression works
    decompressed = lzo.decompress(compressed[4:], False, original_length)
    assert decompressed == test_data