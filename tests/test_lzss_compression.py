import pytest
from src.lzss_compression import LZSSCompressor

def test_lzss_compression_basic():
    """Test basic compression and decompression"""
    compressor = LZSSCompressor()
    test_data = b"HELLO HELLO WORLD"
    
    # Compress
    compressed = compressor.compress(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzss_compression_repeated_pattern():
    """Test compression with repeated patterns"""
    compressor = LZSSCompressor()
    test_data = b"ABCABCABCABCABC"
    
    # Compress
    compressed = compressor.compress(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzss_compression_empty_input():
    """Test compression with empty input"""
    compressor = LZSSCompressor()
    test_data = b""
    
    # Compress
    compressed = compressor.compress(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzss_compression_long_input():
    """Test compression with a longer, more complex input"""
    compressor = LZSSCompressor()
    test_data = b"Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 10
    
    # Compress
    compressed = compressor.compress(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzss_compression_different_window_sizes():
    """Test compression with different window sizes"""
    window_sizes = [512, 1024, 4096]
    test_data = b"HELLO HELLO WORLD HELLO HELLO WORLD"
    
    for window_size in window_sizes:
        compressor = LZSSCompressor(window_size=window_size)
        
        # Compress
        compressed = compressor.compress(test_data)
        
        # Decompress
        decompressed = compressor.decompress(compressed)
        
        assert decompressed == test_data