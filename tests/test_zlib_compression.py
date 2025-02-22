import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data

def test_compression_decompression():
    """Test basic compression and decompression"""
    original_data = "Hello, Zlib compression!"
    compressed = compress_data(original_data)
    decompressed = decompress_data(compressed)
    
    assert decompressed.decode('utf-8') == original_data

def test_binary_data_compression():
    """Test compression with binary data"""
    binary_data = b'\x00\x01\x02\x03\xff'
    compressed = compress_data(binary_data)
    decompressed = decompress_data(compressed)
    
    assert decompressed == binary_data

def test_different_compression_levels():
    """Test different compression levels"""
    data = "Test compression levels" * 100
    
    # Test various compression levels
    compressed_levels = [compress_data(data, level) for level in range(10)]
    
    # Verify that compressed sizes are different and can be decompressed
    for level, compressed in enumerate(compressed_levels):
        decompressed = decompress_data(compressed)
        assert decompressed.decode('utf-8') == data
        
        if level > 0:
            assert len(compressed_levels[level-1]) != len(compressed)

def test_empty_input():
    """Test compression and decompression of empty data"""
    empty_data = ""
    compressed = compress_data(empty_data)
    decompressed = decompress_data(compressed)
    
    assert decompressed.decode('utf-8') == empty_data

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data("not bytes")

def test_invalid_compression_level():
    """Test error handling for invalid compression levels"""
    with pytest.raises(ValueError):
        compress_data("test", compression_level=10)
    
    with pytest.raises(ValueError):
        compress_data("test", compression_level=-1)

def test_invalid_compressed_data():
    """Test error handling for invalid compressed data"""
    with pytest.raises(zlib.error):
        decompress_data(b'invalid compressed data')