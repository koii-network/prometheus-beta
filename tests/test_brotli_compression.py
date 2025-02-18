import pytest
import brotli
from src.brotli_compression import compress_brotli, decompress_brotli

def test_brotli_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, Brotli compression!"
    compressed = compress_brotli(original_data)
    assert compressed != original_data
    assert len(compressed) < len(original_data)
    
    decompressed = decompress_brotli(compressed)
    assert decompressed == original_data

def test_brotli_compression_string():
    """Test compression with string input"""
    original_data = "Hello, World!"
    compressed = compress_brotli(original_data)
    decompressed = decompress_brotli(compressed)
    assert decompressed.decode('utf-8') == original_data

def test_brotli_compression_quality():
    """Test different compression qualities"""
    data = b"Test compression quality"
    
    # Test default quality (11)
    compressed_high = compress_brotli(data)
    
    # Test lower quality
    compressed_low = compress_brotli(data, quality=1)
    
    assert len(compressed_high) <= len(compressed_low)

def test_brotli_compression_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        compress_brotli(123)
    
    with pytest.raises(ValueError):
        compress_brotli(b"test", quality=12)
    
    with pytest.raises(TypeError):
        decompress_brotli("not bytes")

def test_brotli_decompress_error():
    """Test decompression error handling"""
    with pytest.raises(brotli.Error):
        decompress_brotli(b"invalid compressed data")