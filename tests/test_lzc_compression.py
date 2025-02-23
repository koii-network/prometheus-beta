"""
Unit tests for LZC compression and decompression functions.
"""

import pytest
import sys
import os

# Ensure src directory is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzc_compression import lzc_compress, lzc_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression of a simple string."""
    original_data = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzc_compress(original_data)
    decompressed = lzc_decompress(compressed)
    assert decompressed.decode('utf-8') == original_data

def test_byte_data_compression_decompression():
    """Test compression and decompression of byte data."""
    original_data = b'\x01\x02\x03\x01\x02\x03\x04\x05'
    compressed = lzc_compress(original_data)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original_data

def test_repeated_pattern_compression():
    """Test compression of data with repeated patterns."""
    original_data = "AAAAAAAAAABBBBBBBBBB"
    compressed = lzc_compress(original_data)
    decompressed = lzc_decompress(compressed)
    assert decompressed.decode('utf-8') == original_data

def test_empty_input_error():
    """Test error handling for empty input."""
    with pytest.raises(ValueError):
        lzc_compress("")
    with pytest.raises(ValueError):
        lzc_decompress([])

def test_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        lzc_compress(123)
    with pytest.raises(TypeError):
        lzc_decompress([1, 2, "3"])

def test_roundtrip_compression():
    """Test multiple roundtrip compressions."""
    test_strings = [
        "hello world",
        "python is awesome",
        "compression algorithms are interesting",
        "\x00\x01\x02\x03\x04"
    ]
    
    for original in test_strings:
        compressed = lzc_compress(original)
        decompressed = lzc_decompress(compressed)
        assert decompressed.decode('utf-8') == original

def test_large_input():
    """Test compression of a large input."""
    large_input = "REPEATREPEATREPEATREPEAT" * 1000
    compressed = lzc_compress(large_input)
    decompressed = lzc_decompress(compressed)
    assert decompressed.decode('utf-8') == large_input