"""
Test suite for LZP Compression Algorithm.

This module contains comprehensive tests for the LZP compression implementation,
covering various scenarios and edge cases.
"""

import pytest
import random
import string

from src.lzp_compression import LZPCompressor, compress_lzp, decompress_lzp

def generate_random_data(length):
    """Generate random data for testing."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length)).encode('utf-8')

def test_lzp_compression_basic():
    """Test basic compression and decompression."""
    test_data = b"hello world hello world"
    compressor = LZPCompressor()
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data, "Compression and decompression should be reversible"

def test_lzp_compression_empty_input():
    """Test compression and decompression with empty input."""
    compressor = LZPCompressor()
    
    compressed_empty = compressor.compress(b'')
    decompressed_empty = compressor.decompress(compressed_empty)
    
    assert compressed_empty == b''
    assert decompressed_empty == b''

def test_lzp_compression_random_data():
    """Test compression with random data of various lengths."""
    for length in [10, 100, 1000, 10000]:
        random_data = generate_random_data(length)
        compressed = compress_lzp(random_data)
        decompressed = decompress_lzp(compressed)
        
        assert decompressed == random_data, f"Failed for data length {length}"

def test_lzp_compression_different_contexts():
    """Test compression with different context lengths."""
    test_data = b"this is a test string for multiple contexts"
    
    for context_length in [4, 8, 16]:
        compressor = LZPCompressor(context_length=context_length)
        compressed = compressor.compress(test_data)
        decompressed = compressor.decompress(compressed)
        
        assert decompressed == test_data, f"Failed for context length {context_length}"

def test_lzp_compression_string_input():
    """Test compression with string input."""
    test_string = "hello world! 你好世界!"
    compressed = compress_lzp(test_string)
    decompressed = decompress_lzp(compressed)
    
    assert decompressed == test_string.encode('utf-8'), "String compression failed"

def test_lzp_compression_repeated_patterns():
    """Test compression of data with repeated patterns."""
    repeated_data = b"abcabcabcabcabcabcabcabc" * 10
    compressed = compress_lzp(repeated_data)
    decompressed = decompress_lzp(compressed)
    
    assert decompressed == repeated_data, "Repeated pattern compression failed"

def test_lzp_compression_binary_data():
    """Test compression of binary data."""
    binary_data = bytes([random.randint(0, 255) for _ in range(1000)])
    compressed = compress_lzp(binary_data)
    decompressed = decompress_lzp(compressed)
    
    assert decompressed == binary_data, "Binary data compression failed"