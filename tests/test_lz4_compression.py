import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lz4_compression import lz4_compress, lz4_decompress

def test_lz4_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, world! Hello, world!"
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    assert decompressed == original_data

def test_lz4_compression_repeated_sequence():
    """Test compression with repeated sequences"""
    original_data = b"ABCABCABCABCABC"
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    assert decompressed == original_data

def test_lz4_compression_empty_input():
    """Test compression and decompression of empty input"""
    original_data = b""
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    assert decompressed == original_data

def test_lz4_compression_long_input():
    """Test compression of a longer input"""
    original_data = b"This is a longer test string with some repetition " * 100
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    assert decompressed == original_data

def test_lz4_compression_type_error():
    """Test that type errors are raised for invalid inputs"""
    with pytest.raises(TypeError):
        lz4_compress(123)
    
    with pytest.raises(TypeError):
        lz4_decompress(123)

def test_lz4_compression_string_input():
    """Test compression with string input"""
    original_data = "Hello, world!"
    compressed = lz4_compress(original_data)
    decompressed = lz4_decompress(compressed)
    assert decompressed == original_data.encode('utf-8')