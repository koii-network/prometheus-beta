import pytest
from src.lz78_compression import lz78_compress, lz78_decompress

def test_lz78_compression_basic():
    """Test basic LZ78 compression and decompression."""
    test_string = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lz78_compress(test_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == test_string

def test_lz78_empty_string():
    """Test compression and decompression of an empty string."""
    test_string = ""
    compressed = lz78_compress(test_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == test_string
    assert compressed == []

def test_lz78_single_character():
    """Test compression and decompression of a single character."""
    test_string = "A"
    compressed = lz78_compress(test_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == test_string

def test_lz78_repeated_pattern():
    """Test compression of a string with repeated patterns."""
    test_string = "ABABABABABAB"
    compressed = lz78_compress(test_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == test_string

def test_lz78_unique_characters():
    """Test compression of a string with no repeating patterns."""
    test_string = "ABCDEFGHIJKLM"
    compressed = lz78_compress(test_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == test_string

def test_lz78_complex_string():
    """Test compression of a more complex string."""
    test_string = "Hello, hello, hello, world!"
    compressed = lz78_compress(test_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == test_string