import pytest
from src.lz78_compression import lz78_compress, lz78_decompress

def test_lz78_compression_basic():
    # Basic compression and decompression
    input_string = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lz78_compress(input_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == input_string

def test_lz78_empty_string():
    # Test empty string
    assert lz78_compress('') == []
    assert lz78_decompress([]) == ''

def test_lz78_single_character():
    # Test single character
    input_string = "A"
    compressed = lz78_compress(input_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == input_string

def test_lz78_repeated_sequences():
    # Test string with repeated sequences
    input_string = "ABABABABABAB"
    compressed = lz78_compress(input_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == input_string

def test_lz78_complex_string():
    # Test a more complex string
    input_string = "Hello, hello, hello, world!"
    compressed = lz78_compress(input_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == input_string

def test_lz78_compression_ratio():
    # Verify that compression works for strings with repetition
    input_string = "AAAAAAAAAAAAAAAAA"
    compressed = lz78_compress(input_string)
    assert len(compressed) < len(input_string)
    decompressed = lz78_decompress(compressed)
    assert decompressed == input_string