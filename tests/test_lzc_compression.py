"""
Unit tests for LZC compression and decompression functions.
"""

import pytest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzc_compression import lzc_compress, lzc_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression of simple string."""
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzc_compress(original)
    decompressed = bytes(lzc_decompress(compressed)).decode('utf-8')
    assert decompressed == original

def test_byte_data_compression():
    """Test compression and decompression of byte data."""
    original = b'\x01\x02\x03\x01\x02\x03\x04\x05'
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_repeated_pattern():
    """Test compression of highly repetitive data."""
    original = "AAAAAAAAAAAAAAAAA"
    compressed = lzc_compress(original)
    decompressed = bytes(lzc_decompress(compressed)).decode('utf-8')
    assert decompressed == original

def test_empty_input_compression():
    """Test handling of empty input for compression."""
    with pytest.raises(ValueError):
        lzc_compress("")

def test_empty_input_decompression():
    """Test handling of empty input for decompression."""
    with pytest.raises(ValueError):
        lzc_decompress([])

def test_invalid_input_types():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        lzc_compress(123)
    
    with pytest.raises(TypeError):
        lzc_decompress("not a list")

def test_unicode_compression():
    """Test compression of unicode string."""
    original = "Hello, 世界!"
    compressed = lzc_compress(original)
    decompressed = bytes(lzc_decompress(compressed)).decode('utf-8')
    assert decompressed == original

def test_large_repeated_data():
    """Test compression of large repeated data."""
    original = "x" * 1000
    compressed = lzc_compress(original)
    decompressed = bytes(lzc_decompress(compressed)).decode('utf-8')
    assert decompressed == original

def test_complex_pattern():
    """Test compression of more complex pattern."""
    original = "ABABABABABABABABABAB"
    compressed = lzc_compress(original)
    decompressed = bytes(lzc_decompress(compressed)).decode('utf-8')
    assert decompressed == original