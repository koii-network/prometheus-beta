import pytest
from src.lzc_compression import lzc_compress, lzc_decompress

def test_basic_compression_and_decompression():
    # Test basic string compression and decompression
    original = "HELLO WORLD"
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_repeated_patterns():
    # Test compression of repeated patterns
    original = "AAAAAAAAAABBBBBBBBBB"
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_byte_data():
    # Test compression of byte data
    original = b'\x01\x02\x03\x01\x02\x03\x04'
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_empty_input():
    # Test compression and decompression of empty input
    original = ""
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_single_character():
    # Test compression and decompression of single character
    original = "A"
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_long_repeated_sequence():
    # Test compression of very long repeated sequence
    original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 100
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed).decode('utf-8')
    assert decompressed == original