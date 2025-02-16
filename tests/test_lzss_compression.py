import pytest
from src.lzss_compression import LZSSCompressor

def test_lzss_compression_basic():
    """Test basic compression and decompression"""
    compressor = LZSSCompressor()
    original_data = b"HELLO WORLD! HELLO WORLD!"
    
    # Compress
    compressed = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == original_data

def test_lzss_compression_repeated_pattern():
    """Test compression with repeated patterns"""
    compressor = LZSSCompressor()
    original_data = b"abcabcabcabc" * 10
    
    # Compress
    compressed = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == original_data

def test_lzss_compression_empty_input():
    """Test compression with empty input"""
    compressor = LZSSCompressor()
    original_data = b""
    
    # Compress
    compressed = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == original_data

def test_lzss_compression_text_input():
    """Test compression with text input"""
    compressor = LZSSCompressor()
    original_data = "Hello, world! This is a test of LZSS compression."
    
    # Compress
    compressed = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed.decode('utf-8') == original_data

def test_lzss_compression_different_window_sizes():
    """Test compression with different window sizes"""
    test_cases = [
        (1024, b"abcdefghijklmnopqrstuvwxyz" * 20),
        (8192, b"repeated data " * 100)
    ]
    
    for window_size, original_data in test_cases:
        compressor = LZSSCompressor(window_size=window_size)
        
        # Compress
        compressed = compressor.compress(original_data)
        
        # Decompress
        decompressed = compressor.decompress(compressed)
        
        assert decompressed == original_data