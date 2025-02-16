import pytest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.lzma2_compression import lzma2_compress, lzma2_decompress

def test_lzma2_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, this is a test string for LZMA2 compression!"
    compressed = lzma2_compress(original_data)
    decompressed = lzma2_decompress(compressed)
    
    assert decompressed == original_data

def test_lzma2_compression_string():
    """Test compression with string input"""
    original_data = "Hello, world! 🌍"
    compressed = lzma2_compress(original_data)
    decompressed = lzma2_decompress(compressed)
    
    assert decompressed == original_data.encode('utf-8')

def test_lzma2_compression_levels():
    """Test different compression levels"""
    data = b"Repeated data " * 100
    
    compressed_levels = [
        lzma2_compress(data, level) 
        for level in range(10)
    ]
    
    # Verify compression works at all levels
    for level, compressed in enumerate(compressed_levels):
        decompressed = lzma2_decompress(compressed)
        assert decompressed == data

def test_lzma2_compression_error_handling():
    """Test error handling for invalid inputs"""
    # Test non-bytes/str input
    with pytest.raises(TypeError):
        lzma2_compress(123)
    
    # Test invalid compression level
    with pytest.raises(ValueError):
        lzma2_compress(b"test", -1)
    
    with pytest.raises(ValueError):
        lzma2_compress(b"test", 10)
    
    # Test invalid decompression input
    with pytest.raises(TypeError):
        lzma2_decompress("not bytes")

def test_lzma2_large_data_compression():
    """Test compression with larger data"""
    large_data = b"Large test data " * 10000
    compressed = lzma2_compress(large_data)
    decompressed = lzma2_decompress(compressed)
    
    assert decompressed == large_data
    assert len(compressed) < len(large_data)  # Compression should reduce size for repeated data