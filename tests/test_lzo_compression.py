"""
Tests for LZO Compression and Decompression
"""

import pytest
from src.lzo_compression import compress_lzo, decompress_lzo

def test_compress_decompress_basic():
    """Test basic compression and decompression"""
    original_data = b"hello world hello world"
    compressed = compress_lzo(original_data)
    decompressed = decompress_lzo(compressed)
    
    assert decompressed == original_data

def test_compress_decompress_repeated_pattern():
    """Test compression with repeated patterns"""
    original_data = b"ABCABCABCABCABC"
    compressed = compress_lzo(original_data)
    decompressed = decompress_lzo(compressed)
    
    assert decompressed == original_data

def test_compress_decompress_large_data():
    """Test compression with larger data"""
    original_data = b"Test data " * 1000
    compressed = compress_lzo(original_data)
    decompressed = decompress_lzo(compressed)
    
    assert decompressed == original_data

def test_compress_invalid_input_type():
    """Test compression with invalid input type"""
    with pytest.raises(TypeError):
        compress_lzo("not bytes")

def test_decompress_invalid_input_type():
    """Test decompression with invalid input type"""
    with pytest.raises(TypeError):
        decompress_lzo("not bytes")

def test_compress_empty_input():
    """Test compression with empty input"""
    with pytest.raises(ValueError):
        compress_lzo(b"")

def test_decompress_empty_input():
    """Test decompression with empty input"""
    with pytest.raises(ValueError):
        decompress_lzo(b"")

def test_binary_data_compression():
    """Test compression of binary data"""
    original_data = bytes([0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5])
    compressed = compress_lzo(original_data)
    decompressed = decompress_lzo(compressed)
    
    assert decompressed == original_data