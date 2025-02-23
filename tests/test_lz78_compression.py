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
    """Test that the dictionary is built correctly during compression."""
    input_str = "abababab"
    compressed = lz78_compress(input_str)
    
    # Verify the compression produces the expected tokens
    expected_tokens = [
        (0, 'a'),   # First 'a'
        (0, 'b'),   # First 'b'
        (1, 'a'),   # Sequence 'ab'
        (3, 'b'),   # Sequence 'bab'
        (2, 'a'),   # Sequence 'aba'
        (5, 'b')    # Sequence 'abab'
    ]
    
    assert compressed == expected_tokens
    assert lz78_decompress(compressed) == input_str