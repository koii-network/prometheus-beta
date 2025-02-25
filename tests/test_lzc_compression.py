"""
Unit tests for LZC compression and decompression functions.
"""

import pytest
from src.lzc_compression import lzc_compress, lzc_decompress

def test_compress_simple_string():
    """Test compression of a simple string."""
    input_data = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzc_compress(input_data)
    assert len(compressed) < len(input_data)
    decompressed = lzc_decompress(compressed)
    assert decompressed.decode('utf-8') == input_data

def test_compress_repeated_pattern():
    """Test compression of data with repeated patterns."""
    input_data = "ABABABABABABABABAB"
    compressed = lzc_compress(input_data)
    assert len(compressed) < len(input_data)
    decompressed = lzc_decompress(compressed)
    assert decompressed.decode('utf-8') == input_data

def test_compress_bytes():
    """Test compression of raw bytes."""
    input_data = b'\x01\x02\x03\x01\x02\x03\x01\x02\x03'
    compressed = lzc_compress(input_data)
    assert len(compressed) < len(input_data)
    decompressed = lzc_decompress(compressed)
    assert decompressed == input_data

def test_compress_empty_input():
    """Test handling of empty input."""
    with pytest.raises(ValueError, match="Input cannot be empty"):
        lzc_compress(b'')
    with pytest.raises(ValueError, match="Input cannot be empty"):
        lzc_decompress([])

def test_compress_invalid_input_type():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError, match="Input must be a string or bytes"):
        lzc_compress(123)
    with pytest.raises(TypeError, match="Input must be a list of integer codes"):
        lzc_decompress(123)

def test_round_trip_compression():
    """Comprehensive test of compression and decompression."""
    test_cases = [
        "Hello, world!",
        "aaaaaaaaaa",
        "abcdefghijklmnopqrstuvwxyz",
        "The quick brown fox jumps over the lazy dog",
        b'\x00\x01\x02\x03\x04\x05'
    ]
    
    for input_data in test_cases:
        # For bytes and strings
        compressed = lzc_compress(input_data)
        
        # Convert to bytes if string
        if isinstance(input_data, str):
            input_data = input_data.encode('utf-8')
        
        decompressed = lzc_decompress(compressed)
        assert decompressed == input_data, f"Failed for input: {input_data}"