import pytest
from src.lzss_compression import LZSSCompressor

def test_lzss_compression_basic():
    """Test basic compression and decompression"""
    compressor = LZSSCompressor()
    original_data = b"hello world hello world"
    
    # Compress
    compressed = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == original_data

def test_lzss_compression_repeated_sequence():
    """Test compression of highly repetitive data"""
    compressor = LZSSCompressor()
    original_data = b"AAAAAAAAAABBBBBBBBBB" * 10
    
    # Compress
    compressed = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == original_data

def test_lzss_compression_empty_input():
    """Test compression and decompression of empty input"""
    compressor = LZSSCompressor()
    original_data = b""
    
    # Compress
    compressed = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == original_data

def test_lzss_compression_complex_data():
    """Test compression of more complex data"""
    compressor = LZSSCompressor()
    original_data = b"The quick brown fox jumps over the lazy dog " * 5
    
    # Compress
    compressed = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == original_data

def test_lzss_compression_string_input():
    """Test compression with string input"""
    compressor = LZSSCompressor()
    original_data = "hello world hello world"
    
    # Compress
    compressed = compressor.compress(original_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == original_data.encode('utf-8')

def test_lzss_compression_custom_window_sizes():
    """Test compression with different window and lookahead sizes"""
    # Test with smaller window
    compressor_small = LZSSCompressor(window_size=256, lookahead_size=8)
    original_data = b"hello world hello world" * 10
    
    # Compress
    compressed_small = compressor_small.compress(original_data)
    
    # Decompress
    decompressed_small = compressor_small.decompress(compressed_small)
    
    assert decompressed_small == original_data