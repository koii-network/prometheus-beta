import pytest
from src.lzss_compression import LZSS

def test_lzss_basic_compression_decompression():
    """Test basic compression and decompression."""
    lzss = LZSS()
    original_data = b"HELLO HELLO WORLD"
    
    # Compress
    compressed = lzss.compress(original_data)
    
    # Decompress
    decompressed = lzss.decompress(compressed)
    
    assert decompressed == original_data

def test_lzss_repeated_pattern():
    """Test compression with repeated patterns."""
    lzss = LZSS()
    original_data = b"ABCABCABCABC" * 10
    
    # Compress
    compressed = lzss.compress(original_data)
    
    # Decompress
    decompressed = lzss.decompress(compressed)
    
    assert decompressed == original_data

def test_lzss_different_window_sizes():
    """Test compression with different window sizes."""
    test_data = b"Hello, this is a test of LZSS compression with different window sizes!"
    
    # Test various window sizes
    for window_size in [128, 256, 512, 1024]:
        lzss = LZSS(window_size=window_size)
        
        # Compress
        compressed = lzss.compress(test_data)
        
        # Decompress
        decompressed = lzss.decompress(compressed)
        
        assert decompressed == test_data

def test_lzss_string_input():
    """Test compression with string input."""
    lzss = LZSS()
    original_data = "Hello, world! This is a test of LZSS compression."
    
    # Compress
    compressed = lzss.compress(original_data)
    
    # Decompress
    decompressed = lzss.decompress(compressed)
    
    assert decompressed.decode('utf-8') == original_data

def test_lzss_empty_input():
    """Test compression with empty input."""
    lzss = LZSS()
    original_data = b""
    
    # Compress
    compressed = lzss.compress(original_data)
    
    # Decompress
    decompressed = lzss.decompress(compressed)
    
    assert decompressed == original_data