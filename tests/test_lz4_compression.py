import pytest
from src.lz4_compression import lz4_compress, lz4_decompress

def test_lz4_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, world! Hello, world!"
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed == original_data

def test_lz4_compression_repeated_patterns():
    """Test compression with repeated patterns"""
    original_data = b"ABCABCABCABCABCABC" * 10
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed == original_data

def test_lz4_compression_empty_input():
    """Test compression and decompression of empty input"""
    original_data = b""
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed == original_data

def test_lz4_compression_string_input():
    """Test compression with string input"""
    original_data = "Hello, world! This is a test string."
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed.decode('utf-8') == original_data

def test_lz4_compression_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        lz4_compress(123)
    
    with pytest.raises(TypeError):
        lz4_decompress(123)

def test_lz4_compression_large_input():
    """Test compression and decompression of a large input"""
    original_data = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 1000
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed == original_data