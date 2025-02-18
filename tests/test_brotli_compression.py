import pytest
import brotli
from src.brotli_compression import compress_data, decompress_data

def test_compression_decompression():
    """Test basic compression and decompression cycle"""
    original_data = b"Hello, this is a test string for Brotli compression!"
    
    # Compress the data
    compressed = compress_data(original_data)
    
    # Verify compression actually reduced size
    assert len(compressed) < len(original_data)
    
    # Decompress and verify original data
    decompressed = decompress_data(compressed)
    assert decompressed == original_data

def test_compression_quality():
    """Test different compression qualities"""
    test_data = b"This is a test string to check different compression qualities"
    
    # Test various quality levels
    for quality in [0, 5, 11]:
        compressed = compress_data(test_data, quality)
        decompressed = decompress_data(compressed)
        assert decompressed == test_data

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compress_data("Not bytes")
    
    with pytest.raises(TypeError):
        decompress_data("Not bytes")

def test_invalid_compression_quality():
    """Test error handling for invalid compression quality"""
    test_data = b"Test compression quality"
    
    with pytest.raises(ValueError):
        compress_data(test_data, -1)
    
    with pytest.raises(ValueError):
        compress_data(test_data, 12)

def test_empty_data():
    """Test compression and decompression of empty bytes"""
    empty_data = b""
    
    compressed = compress_data(empty_data)
    decompressed = decompress_data(compressed)
    
    assert decompressed == empty_data