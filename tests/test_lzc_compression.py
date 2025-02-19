import pytest
from src.lzc_compression import lzc_compress, lzc_decompress

def test_lzc_compression_basic():
    """Test basic compression and decompression"""
    original = b'ABCABCABCABCABCABC'
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_lzc_compression_string():
    """Test compression with string input"""
    original = 'Hello, world! Hello, world!'
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original.encode('utf-8')

def test_lzc_compression_repeating_pattern():
    """Test compression with highly repetitive data"""
    original = b'\x01\x01\x01\x01\x01\x01\x01\x01'
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_lzc_compression_empty_input():
    """Test compression with empty input"""
    original = b''
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_lzc_compression_random_data():
    """Test compression with random data"""
    original = b'\x45\x23\x67\x89\x12\x34\x56\x78'
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_large_compression():
    """Test compression with a larger input"""
    original = b'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 100
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original