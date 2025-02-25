"""
Tests for LZSS Compression Algorithm
"""

import pytest
import random
import string
from src.lzss_compression import LZSSCompressor

def generate_random_string(length):
    """Generate a random string of specified length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def test_lzss_compressor_initialization():
    """Test initialization of LZSSCompressor."""
    compressor = LZSSCompressor()
    assert compressor.window_size == 4096
    assert compressor.lookahead_size == 16
    assert compressor.min_match_length == 3

def test_lzss_simple_compression_decompression():
    """Test basic compression and decompression."""
    compressor = LZSSCompressor()
    original_text = "hello world hello world"
    
    # Compress
    compressed = compressor.compress(original_text)
    assert compressed is not None
    
    # Verify correct decompression
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == original_text

def test_lzss_empty_input():
    """Test handling of empty input."""
    compressor = LZSSCompressor()
    
    # Empty string
    empty_str = ""
    compressed_empty = compressor.compress(empty_str)
    assert compressed_empty == b''
    decompressed_empty = compressor.decompress(compressed_empty)
    assert decompressed_empty == b''

def test_lzss_random_data_compression():
    """Test compression with random data."""
    compressor = LZSSCompressor()
    
    # Generate random strings of different lengths
    for length in [10, 100, 1000]:
        random_str = generate_random_string(length)
        
        # Compress
        compressed = compressor.compress(random_str)
        
        # Decompress
        decompressed = compressor.decompress(compressed)
        
        assert decompressed.decode('utf-8') == random_str

def test_lzss_repeated_pattern():
    """Test compression of highly repetitive data."""
    compressor = LZSSCompressor()
    repeated_text = "abcabcabcabcabcabc" * 10
    
    # Compress
    compressed = compressor.compress(repeated_text)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == repeated_text

def test_lzss_bytes_input():
    """Test compression of byte input."""
    compressor = LZSSCompressor()
    byte_data = b'\x00\x01\x02\x03\x00\x01\x02\x03'
    
    # Compress
    compressed = compressor.compress(byte_data)
    
    # Decompress
    decompressed = compressor.decompress(compressed)
    assert decompressed == byte_data

def test_lzss_invalid_input_types():
    """Test handling of invalid input types."""
    compressor = LZSSCompressor()
    
    # Test invalid input type for compression
    with pytest.raises(TypeError):
        compressor.compress(123)
    
    # Test invalid input type for decompression
    with pytest.raises(TypeError):
        compressor.decompress(123)

def test_lzss_custom_window_and_lookahead():
    """Test compression with custom window and lookahead sizes."""
    compressor = LZSSCompressor(window_size=1024, lookahead_size=8, min_match_length=2)
    assert compressor.window_size == 1024
    assert compressor.lookahead_size == 8
    assert compressor.min_match_length == 2
    
    test_text = "hello world " * 10
    compressed = compressor.compress(test_text)
    decompressed = compressor.decompress(compressed)
    assert decompressed.decode('utf-8') == test_text