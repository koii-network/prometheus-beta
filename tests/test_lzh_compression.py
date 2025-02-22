import pytest
import random
from src.lzh_compression import LZHCompressor

def test_lzh_compression_basic():
    """Test basic compression and decompression"""
    compressor = LZHCompressor()
    test_data = b"Hello, world! This is a test of LZH compression."
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzh_compression_repeated_data():
    """Test compression of data with repeated patterns"""
    compressor = LZHCompressor()
    test_data = b"ABCABCABCABCABCABCABC" * 10
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzh_compression_random_data():
    """Test compression of random data"""
    compressor = LZHCompressor()
    test_data = bytes(random.randint(0, 255) for _ in range(1000))
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzh_compression_empty_data():
    """Test compression of empty data"""
    compressor = LZHCompressor()
    test_data = b""
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzh_compression_large_data():
    """Test compression of large data"""
    compressor = LZHCompressor()
    test_data = b"Large data test " * 1000
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data

def test_lzh_compression_string_input():
    """Test compression with string input"""
    compressor = LZHCompressor()
    test_data = "Hello, world! This is a test of LZH compression."
    
    compressed = compressor.compress(test_data)
    decompressed = compressor.decompress(compressed)
    
    assert decompressed == test_data.encode('utf-8')