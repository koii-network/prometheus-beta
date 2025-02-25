import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data


def test_compress_string():
    """Test compression of a string"""
    original = "Hello, World! This is a test of Zlib compression."
    compressed = compress_data(original)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original.encode('utf-8'))


def test_compress_bytes():
    """Test compression of bytes"""
    original = b"Hello, World! This is a test of Zlib compression."
    compressed = compress_data(original)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original)


def test_compress_with_level():
    """Test compression with specific compression levels"""
    original = "Hello, World!" * 100  # Longer text to show compression difference
    
    # Test different compression levels
    compressed_0 = compress_data(original, compression_level=0)
    compressed_6 = compress_data(original, compression_level=6)
    compressed_9 = compress_data(original, compression_level=9)
    
    assert len(compressed_0) >= len(compressed_6)
    assert len(compressed_6) >= len(compressed_9)


def test_decompress():
    """Test full compression and decompression cycle"""
    original = "Hello, World! This is a test of Zlib compression."
    compressed = compress_data(original)
    decompressed = decompress_data(compressed)
    
    assert decompressed.decode('utf-8') == original


def test_compress_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        compress_data(None)


def test_compress_invalid_compression_level():
    """Test error handling for invalid compression levels"""
    original = "Hello, World!"
    
    with pytest.raises(TypeError):
        compress_data(original, compression_level="high")
    
    with pytest.raises(ValueError):
        compress_data(original, compression_level=-1)
    
    with pytest.raises(ValueError):
        compress_data(original, compression_level=10)


def test_decompress_invalid_input():
    """Test error handling for invalid decompression input"""
    with pytest.raises(TypeError):
        decompress_data("not bytes")
    
    with pytest.raises(zlib.error):
        decompress_data(b"invalid compressed data")


def test_compress_empty_input():
    """Test compression of empty input"""
    original = ""
    compressed = compress_data(original)
    decompressed = decompress_data(compressed)
    
    assert decompressed.decode('utf-8') == original


def test_large_data_compression():
    """Test compression of large data"""
    original = "This is a large text " * 1000
    compressed = compress_data(original)
    decompressed = decompress_data(compressed)
    
    assert decompressed.decode('utf-8') == original