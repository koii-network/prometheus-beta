import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzw_compression import lzw_compress, lzw_decompress

def test_lzw_compression_basic():
    """Test basic string compression and decompression"""
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lzw_bytes_compression():
    """Test compression with bytes input"""
    original = b"Hello, world! Hello, world!"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_empty_input():
    """Test compression and decompression of empty input"""
    original = ""
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lzw_repeated_patterns():
    """Test compression of repeated patterns"""
    original = "ABABABABABABABABAB"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lzw_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        lzw_compress(123)
    
    with pytest.raises(TypeError):
        lzw_decompress("not a list")
    
    with pytest.raises(TypeError):
        lzw_decompress([1, "2", 3])

def test_lzw_invalid_compressed_data():
    """Test handling of invalid compressed data"""
    with pytest.raises(ValueError):
        lzw_decompress([256, 257, 1000])  # Invalid codes

def test_lzw_compression_reversibility():
    """Test that multiple compression and decompression cycles work"""
    original = "This is a test string with some repeated content!"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed.decode('utf-8') == original