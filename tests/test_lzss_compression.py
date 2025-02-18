import pytest
from src.lzss_compression import LZSSCompressor

def test_lzss_compression_basic():
    compressor = LZSSCompressor()
    
    # Test simple string compression and decompression
    original = "hello world hello world"
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed.decode('utf-8') == original

def test_lzss_compression_repeated_pattern():
    compressor = LZSSCompressor()
    
    # Test compression with many repeated patterns
    original = "abcabcabcabcabcabc" * 10
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed.decode('utf-8') == original

def test_lzss_compression_bytes():
    compressor = LZSSCompressor()
    
    # Test compression with bytes
    original = b'\x00\x01\x02\x00\x01\x02\x00\x01\x02'
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == original

def test_lzss_compression_empty_input():
    compressor = LZSSCompressor()
    
    # Test empty string/bytes
    original = ""
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed.decode('utf-8') == original

def test_lzss_compression_single_character():
    compressor = LZSSCompressor()
    
    # Test single character input
    original = "a"
    compressed = compressor.compress(original)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed.decode('utf-8') == original

def test_lzss_compression_error_handling():
    compressor = LZSSCompressor()
    
    # Test incomplete compressed data
    with pytest.raises(ValueError):
        compressor.decompress(b'\x00\x01')  # Incomplete compressed token
    
    with pytest.raises(ValueError):
        compressor.decompress(b'\x01')  # Incomplete uncompressed token

def test_lzss_compression_different_window_sizes():
    # Test compression with different window sizes
    sizes = [128, 256, 1024, 4096]
    original = "this is a test string with some repeated content " * 5
    
    for window_size in sizes:
        compressor = LZSSCompressor(window_size=window_size)
        compressed = compressor.compress(original)
        decompressed = compressor.decompress(compressed)
        
        assert decompressed.decode('utf-8') == original