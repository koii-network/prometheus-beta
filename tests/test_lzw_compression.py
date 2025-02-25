"""
Unit tests for LZW Compression Algorithm
"""

import pytest
from src.lzw_compression import lzw_compress, lzw_decompress

def test_lzw_basic_compression_decompression():
    """Test basic compression and decompression cycle"""
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_single_character_string():
    """Test compression and decompression of a single character string"""
    original = "A"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_repeated_pattern():
    """Test compression of a string with repeated patterns"""
    original = "ABABABABAB"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_complex_string():
    """Test compression of a more complex string"""
    original = "Hello, World! This is a test of LZW compression."
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_compress_invalid_input_type():
    """Test that TypeError is raised for non-string input"""
    with pytest.raises(TypeError):
        lzw_compress(12345)
    with pytest.raises(TypeError):
        lzw_compress(["not", "a", "string"])

def test_lzw_decompress_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        lzw_decompress("not a list")
    with pytest.raises(TypeError):
        lzw_decompress(12345)

def test_lzw_compress_empty_string():
    """Test that ValueError is raised for empty string"""
    with pytest.raises(ValueError):
        lzw_compress("")

def test_lzw_decompress_empty_list():
    """Test that ValueError is raised for empty list"""
    with pytest.raises(ValueError):
        lzw_decompress([])

def test_lzw_bidirectional_compression():
    """
    Comprehensive test to ensure multiple cycles 
    of compression and decompression work correctly
    """
    test_strings = [
        "TOBEORNOTTOBEORTOBEORNOT",
        "Hello, World!",
        "abcabcabcabcabcabc",
        "This is a test of LZW compression and decompression."
    ]
    
    for original in test_strings:
        compressed = lzw_compress(original)
        decompressed = lzw_decompress(compressed)
        assert decompressed == original, f"Failed for string: {original}"