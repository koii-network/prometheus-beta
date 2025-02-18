import pytest
from src.lzc_compression import lzc_compress, lzc_decompress

def test_lzc_compression_basic():
    # Test basic string compression and decompression
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_lzc_compression_empty_input():
    # Test empty input
    assert lzc_compress("") == []
    assert lzc_decompress([]) == b''

def test_lzc_compression_single_character():
    # Test single character input
    original = "A"
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_lzc_compression_repeated_sequence():
    # Test input with repeated sequences
    original = "ABABABABAB"
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_lzc_compression_bytes_input():
    # Test bytes input
    original = b'\x01\x02\x03\x01\x02\x03\x04'
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_lzc_compression_long_input():
    # Test longer input with more complex patterns
    original = "The quick brown fox jumps over the lazy dog " * 10
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_lzc_compression_boundary_conditions():
    # Test various boundary conditions
    test_cases = [
        "A" * 1000,  # Long repeated character
        "ABCDEFG" * 100,  # Repeating pattern
        "X" + "Y" * 500  # Mixed pattern
    ]
    
    for case in test_cases:
        compressed = lzc_compress(case)
        decompressed = lzc_decompress(compressed).decode('utf-8')
        assert decompressed == case