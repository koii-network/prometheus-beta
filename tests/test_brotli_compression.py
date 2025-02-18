import pytest
import brotli
from src.brotli_compression import compress_brotli, decompress_brotli

def test_brotli_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, Brotli compression!"
    compressed_data = compress_brotli(original_data)
    
    assert isinstance(compressed_data, bytes)
    assert len(compressed_data) < len(original_data)
    
    decompressed_data = decompress_brotli(compressed_data)
    assert decompressed_data == original_data

def test_brotli_compression_str_input():
    """Test compression with string input"""
    original_data = "Hello, Brotli compression!"
    compressed_data = compress_brotli(original_data)
    
    assert isinstance(compressed_data, bytes)
    
    decompressed_data = decompress_brotli(compressed_data)
    assert decompressed_data == original_data.encode('utf-8')

def test_brotli_compression_levels():
    """Test different compression levels"""
    original_data = b"Test compression with different levels"
    
    for level in range(12):
        compressed_data = compress_brotli(original_data, compression_level=level)
        decompressed_data = decompress_brotli(compressed_data)
        assert decompressed_data == original_data

def test_brotli_compression_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        compress_brotli(123)
    
    with pytest.raises(TypeError):
        decompress_brotli("not bytes")
    
    with pytest.raises(ValueError):
        compress_brotli(b"test", compression_level=12)

def test_brotli_compression_empty_input():
    """Test compression and decompression with empty input"""
    empty_data = b""
    compressed_data = compress_brotli(empty_data)
    
    assert isinstance(compressed_data, bytes)
    
    decompressed_data = decompress_brotli(compressed_data)
    assert decompressed_data == empty_data