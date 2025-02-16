import pytest
import brotli
from src.brotli_compression import compress_with_brotli, decompress_with_brotli

def test_compression_decompression():
    """Test basic compression and decompression cycle"""
    original_data = b"Hello, Brotli compression is amazing!"
    compressed_data = compress_with_brotli(original_data)
    
    assert compressed_data != original_data
    assert len(compressed_data) < len(original_data)
    
    decompressed_data = decompress_with_brotli(compressed_data)
    assert decompressed_data == original_data

def test_compression_quality():
    """Test different compression qualities"""
    data = b"Test data for compression quality"
    
    # Test different compression levels
    for quality in [0, 5, 11]:
        compressed_data = compress_with_brotli(data, quality)
        decompressed_data = decompress_with_brotli(compressed_data)
        assert decompressed_data == data

def test_large_data_compression():
    """Test compression of large data"""
    large_data = b"A" * 10000
    compressed_data = compress_with_brotli(large_data)
    decompressed_data = decompress_with_brotli(compressed_data)
    
    assert decompressed_data == large_data

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compress_with_brotli("Not bytes")
    
    with pytest.raises(TypeError):
        decompress_with_brotli("Not bytes")

def test_invalid_compression_quality():
    """Test error handling for invalid compression quality"""
    data = b"Test data"
    
    with pytest.raises(ValueError):
        compress_with_brotli(data, -1)
    
    with pytest.raises(ValueError):
        compress_with_brotli(data, 12)

def test_empty_data_compression():
    """Test compression and decompression of empty data"""
    empty_data = b""
    compressed_data = compress_with_brotli(empty_data)
    decompressed_data = decompress_with_brotli(compressed_data)
    
    assert decompressed_data == empty_data