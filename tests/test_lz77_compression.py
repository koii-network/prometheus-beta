import pytest
from src.lz77_compression import LZ77Compressor

def test_lz77_compression_basic():
    """Test basic compression and decompression"""
    compressor = LZ77Compressor()
    test_data = b"ABCABCABCABC"
    
    # Compress
    compressed = compressor.compress(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lz77_compression_repeated_pattern():
    """Test compression with repeating patterns"""
    compressor = LZ77Compressor()
    test_data = b"AAAAAAAAAAAAAA"
    
    # Compress
    compressed = compressor.compress(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lz77_compression_string_input():
    """Test compression with string input"""
    compressor = LZ77Compressor()
    test_data = "Hello, world! Hello, world!"
    
    # Compress
    compressed = compressor.compress(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed.decode('utf-8') == test_data

def test_lz77_compression_empty_input():
    """Test compression with empty input"""
    compressor = LZ77Compressor()
    test_data = b""
    
    # Compress
    compressed = compressor.compress(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lz77_compression_random_data():
    """Test compression with random data"""
    compressor = LZ77Compressor()
    test_data = b"The quick brown fox jumps over the lazy dog"
    
    # Compress
    compressed = compressor.compress(test_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_different_window_sizes():
    """Test compression with different window sizes"""
    test_data = b"ABCDEFABCDEFABCDEF"
    
    # Test multiple window sizes
    for window_size in [8, 16, 32, 64]:
        compressor = LZ77Compressor(window_size=window_size)
        
        # Compress
        compressed = compressor.compress(test_data)
        
        # Decompress
        decompressed = compressor.decompress(compressed)
        
        assert decompressed == test_data