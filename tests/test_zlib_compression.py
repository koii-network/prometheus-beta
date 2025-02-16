import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data

def test_compress_decompress_str():
    """Test compression and decompression of a string"""
    original_data = "Hello, world! This is a test of Zlib compression."
    compressed = compress_data(original_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original_data.encode('utf-8'))
    
    decompressed = decompress_data(compressed).decode('utf-8')
    assert decompressed == original_data

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes"""
    original_data = b"Binary data to compress"
    compressed = compress_data(original_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original_data)
    
    decompressed = decompress_data(compressed)
    assert decompressed == original_data

def test_compression_levels():
    """Test different compression levels"""
    data = "Test compression levels"
    
    # Test different compression levels
    for level in range(10):
        compressed = compress_data(data, compression_level=level)
        decompressed = decompress_data(compressed).decode('utf-8')
        assert decompressed == data

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data("not bytes")

def test_invalid_compression_level():
    """Test error handling for invalid compression levels"""
    with pytest.raises(ValueError):
        compress_data("data", compression_level=10)
    
    with pytest.raises(ValueError):
        compress_data("data", compression_level=-1)

def test_decompress_invalid_data():
    """Test decompression of invalid compressed data"""
    with pytest.raises(zlib.error):
        decompress_data(b"Invalid compressed data")