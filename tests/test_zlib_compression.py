import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data

def test_compress_data_basic():
    """Test basic compression of string and bytes"""
    # Test string input
    test_string = "Hello, Zlib compression!"
    compressed = compress_data(test_string)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(test_string.encode('utf-8'))

    # Test bytes input
    test_bytes = b"Hello, Zlib compression!"
    compressed_bytes = compress_data(test_bytes)
    assert isinstance(compressed_bytes, bytes)
    assert len(compressed_bytes) < len(test_bytes)

def test_decompress_data():
    """Test round-trip compression and decompression"""
    test_string = "Hello, Zlib compression!"
    compressed = compress_data(test_string)
    decompressed = decompress_data(compressed)
    assert decompressed == test_string.encode('utf-8')

def test_compression_levels():
    """Test different compression levels"""
    test_data = b"Repeated data " * 100
    
    # Test different compression levels
    for level in range(10):
        compressed = compress_data(test_data, level)
        decompressed = decompress_data(compressed)
        assert decompressed == test_data

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data(123)

def test_invalid_compression_level():
    """Test error handling for invalid compression levels"""
    with pytest.raises(ValueError):
        compress_data("test", -1)
    
    with pytest.raises(ValueError):
        compress_data("test", 10)

def test_decompress_invalid_data():
    """Test decompression of invalid compressed data"""
    with pytest.raises(zlib.error):
        decompress_data(b"Invalid compressed data")

def test_empty_data():
    """Test compression and decompression of empty data"""
    empty_string = ""
    empty_bytes = b""
    
    compressed_str = compress_data(empty_string)
    compressed_bytes = compress_data(empty_bytes)
    
    assert decompress_data(compressed_str) == empty_string.encode('utf-8')
    assert decompress_data(compressed_bytes) == empty_bytes