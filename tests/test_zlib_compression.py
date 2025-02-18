import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data

def test_compress_data_basic():
    """Test basic compression and decompression"""
    original_data = "Hello, World!"
    compressed = compress_data(original_data)
    assert isinstance(compressed, bytes)
    
    # For very small inputs, compression might not reduce size
    # So we'll just check it can be decompressed correctly
    decompressed = decompress_data(compressed)
    assert decompressed.decode('utf-8') == original_data

def test_compress_data_bytes():
    """Test compression with bytes input"""
    original_data = b"Binary data test"
    compressed = compress_data(original_data)
    assert isinstance(compressed, bytes)
    
    decompressed = decompress_data(compressed)
    assert decompressed == original_data

def test_compression_levels():
    """Test different compression levels with a larger dataset"""
    data = "Test compression levels" * 1000  # Large enough data for meaningful comparison
    
    # Test different compression levels
    compressed_0 = compress_data(data, compression_level=0)
    compressed_6 = compress_data(data, compression_level=6)
    compressed_9 = compress_data(data, compression_level=9)
    
    # Higher compression levels should result in smaller compressed data
    assert len(compressed_9) <= len(compressed_6)
    assert len(compressed_6) <= len(compressed_0)

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data("not bytes")

def test_invalid_compression_level():
    """Test error handling for invalid compression levels"""
    with pytest.raises(ValueError):
        compress_data("test", compression_level=-1)
    
    with pytest.raises(ValueError):
        compress_data("test", compression_level=10)

def test_decompression_error():
    """Test error handling for invalid compressed data"""
    with pytest.raises(zlib.error):
        decompress_data(b"invalid compressed data")