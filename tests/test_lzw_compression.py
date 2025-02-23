"""
Test suite for LZW Compression and Decompression
"""

import pytest
from src.lzw_compression import lzw_compress, lzw_decompress

def test_lzw_basic_compression_decompression():
    """Test basic compression and decompression of a simple string"""
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_empty_string_raises_error():
    """Test that empty string raises ValueError"""
    with pytest.raises(ValueError):
        lzw_compress("")

def test_lzw_non_string_input_raises_error():
    """Test that non-string input raises TypeError"""
    with pytest.raises(TypeError):
        lzw_compress(123)

def test_lzw_repeated_patterns():
    """Test compression of a string with repeated patterns"""
    original = "ABABABABABABABABAB"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_single_character_string():
    """Test compression of a single character string"""
    original = "A"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_long_complex_string():
    """Test compression of a longer, more complex string"""
    original = "the quick brown fox jumps over the lazy dog"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_compression_type():
    """Verify that compression returns a list of integers"""
    compressed = lzw_compress("test")
    assert isinstance(compressed, list)
    assert all(isinstance(code, int) for code in compressed)

def test_lzw_invalid_compressed_input():
    """Test that invalid compressed input raises an error"""
    with pytest.raises(ValueError):
        lzw_decompress([9999999])  # Unreasonably large code

def test_lzw_empty_compressed_input():
    """Test that empty compressed input raises an error"""
    with pytest.raises(ValueError):
        lzw_decompress([])

def test_lzw_non_list_input():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError):
        lzw_decompress("not a list")