"""
Test suite for LZ78 compression and decompression functions.
"""

import pytest
from src.lz78_compression import lz78_compress, lz78_decompress


def test_lz78_compress_simple_string():
    """Test compression of a simple repeating string."""
    input_str = "AAAAABBBBCCCC"
    compressed = lz78_compress(input_str)
    decompressed = lz78_decompress(compressed)
    assert decompressed == input_str


def test_lz78_compress_complex_string():
    """Test compression of a more complex string."""
    input_str = "banana banana bo bana"
    compressed = lz78_compress(input_str)
    decompressed = lz78_decompress(compressed)
    assert decompressed == input_str


def test_lz78_compress_empty_string():
    """Test compression and decompression of an empty string raises ValueError."""
    with pytest.raises(ValueError):
        lz78_compress("")


def test_lz78_compress_non_string_input():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError):
        lz78_compress(12345)
    with pytest.raises(TypeError):
        lz78_compress(["not", "a", "string"])


def test_lz78_decompress_invalid_input():
    """Test that invalid compressed data raises exceptions."""
    with pytest.raises(TypeError):
        lz78_decompress("not a list")
    
    # Invalid dictionary index
    with pytest.raises(ValueError):
        lz78_decompress([(999, 'x')])


def test_lz78_compression_symmetry():
    """Ensure compression and decompression are symmetric."""
    test_cases = [
        "hello world",
        "abracadabra",
        "mississippi",
        "aaaabbbccccddddd",
        "",  # Empty string (handled separately due to ValueError)
    ]
    
    for test_str in test_cases[:-1]:  # Exclude empty string
        compressed = lz78_compress(test_str)
        decompressed = lz78_decompress(compressed)
        assert decompressed == test_str


def test_lz78_compression_dictionary_building():
    """Test that the compression produces a valid and complete decompression."""
    input_str = "abababab"
    compressed = lz78_compress(input_str)
    
    # Verify the compression can be correctly decompressed
    decompressed = lz78_decompress(compressed)
    assert decompressed == input_str
    
    # Verify the length of compressed tokens is reasonable
    assert len(compressed) > 0
    assert len(compressed) <= len(input_str)