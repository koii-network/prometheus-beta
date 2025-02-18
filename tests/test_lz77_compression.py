import pytest
from src.lz77_compression import LZ77Compressor

def test_lz77_compress_empty_string():
    """Test compression of an empty string"""
    compressor = LZ77Compressor()
    compressed = compressor.compress("")
    assert compressed == []

def test_lz77_compress_single_character():
    """Test compression of a single character"""
    compressor = LZ77Compressor()
    compressed = compressor.compress("a")
    assert compressed == [(0, 0, 'a')]

def test_lz77_compress_repeated_pattern():
    """Test compression of a repeated pattern"""
    compressor = LZ77Compressor()
    input_str = "ababababab"
    compressed = compressor.compress(input_str)
    
    # Decompress and verify
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == input_str

def test_lz77_full_compression_cycle():
    """Test full compression and decompression cycle"""
    compressor = LZ77Compressor()
    test_strings = [
        "hello world",
        "abcabcabcabc",
        "repeated repeated repeated",
        "python programming is fun"
    ]
    
    for test_str in test_strings:
        compressed = compressor.compress(test_str)
        decompressed = compressor.decompress(compressed)
        assert decompressed.decode('utf-8') == test_str

def test_lz77_byte_compression():
    """Test compression of byte data"""
    compressor = LZ77Compressor()
    test_bytes = b'\x01\x02\x03\x01\x02\x03\x01\x02\x03'
    compressed = compressor.compress(test_bytes)
    decompressed = compressor.decompress(compressed)
    assert decompressed == test_bytes

def test_lz77_different_window_sizes():
    """Test compression with different window sizes"""
    window_sizes = [128, 256, 512, 1024]
    input_str = "this is a test string with some repeated content"
    
    for window_size in window_sizes:
        compressor = LZ77Compressor(window_size=window_size)
        compressed = compressor.compress(input_str)
        decompressed = compressor.decompress(compressed)
        assert decompressed.decode('utf-8') == input_str