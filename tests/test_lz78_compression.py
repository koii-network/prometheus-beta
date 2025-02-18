import pytest
from src.lz78_compression import lz78_compress, lz78_decompress

def test_lz78_empty_string():
    """Test compression and decompression of an empty string."""
    input_str = ''
    compressed = lz78_compress(input_str)
    assert compressed == []
    assert lz78_decompress(compressed) == ''

def test_lz78_simple_string():
    """Test compression and decompression of a simple string."""
    input_str = 'TOBEORNOTTOBEORTOBEORNOT'
    compressed = lz78_compress(input_str)
    decompressed = lz78_decompress(compressed)
    assert decompressed == input_str

def test_lz78_repeating_patterns():
    """Test compression of a string with repeating patterns."""
    input_str = 'ababababababababab'
    compressed = lz78_compress(input_str)
    decompressed = lz78_decompress(compressed)
    assert decompressed == input_str

def test_lz78_single_character():
    """Test compression and decompression of a single character."""
    input_str = 'a'
    compressed = lz78_compress(input_str)
    decompressed = lz78_decompress(compressed)
    assert decompressed == input_str

def test_lz78_complex_string():
    """Test compression of a more complex string."""
    input_str = 'hello world hello hello world'
    compressed = lz78_compress(input_str)
    decompressed = lz78_decompress(compressed)
    assert decompressed == input_str