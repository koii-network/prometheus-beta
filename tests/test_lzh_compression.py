import pytest
from src.lzh_compression import LZHCompressor

def test_lzh_compression_basic():
    """Test basic string compression and decompression"""
    compressor = LZHCompressor()
    test_string = "HELLO WORLD"
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed.decode('utf-8') == test_string

def test_lzh_compression_repeated_patterns():
    """Test compression with repeated patterns"""
    compressor = LZHCompressor()
    test_string = "ABABABABABABAB"
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed.decode('utf-8') == test_string

def test_lzh_compression_binary_data():
    """Test compression with binary data"""
    compressor = LZHCompressor()
    test_bytes = bytes([1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 3])
    
    # Compress
    compressed = compressor.compress(test_bytes)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_bytes

def test_lzh_compression_empty_input():
    """Test compression with empty input"""
    compressor = LZHCompressor()
    test_string = ""
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed.decode('utf-8') == test_string

def test_lzh_compression_long_text():
    """Test compression with longer text"""
    compressor = LZHCompressor()
    test_string = "This is a longer test string with some repeated words to test compression efficiency"
    
    # Compress
    compressed = compressor.compress(test_string)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed.decode('utf-8') == test_string