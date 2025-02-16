import pytest
from src.lzjb_compression import lzjb_compress, lzjb_decompress

def test_lzjb_compress_decompress_simple():
    """Test basic compression and decompression"""
    test_data = b"Hello, world! This is a test of LZJB compression."
    compressed = lzjb_compress(test_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == test_data

def test_lzjb_repeated_data():
    """Test compression with repeated data"""
    test_data = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    compressed = lzjb_compress(test_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == test_data
    assert len(compressed) < len(test_data)  # Ensure compression occurred

def test_lzjb_empty_input():
    """Test compression and decompression of empty input"""
    test_data = b""
    compressed = lzjb_compress(test_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == test_data

def test_lzjb_invalid_input_type():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        lzjb_compress("Not bytes")
    
    with pytest.raises(TypeError):
        lzjb_decompress("Not bytes")

def test_lzjb_complex_data():
    """Test compression with more complex, mixed data"""
    test_data = b"abcdefghijklmnopqrstuvwxyz" * 10
    compressed = lzjb_compress(test_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == test_data

def test_lzjb_binary_data():
    """Test compression with binary data"""
    test_data = bytes(range(256)) * 5
    compressed = lzjb_compress(test_data)
    decompressed = lzjb_decompress(compressed)
    
    assert decompressed == test_data