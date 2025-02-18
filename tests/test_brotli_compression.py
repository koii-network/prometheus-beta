import pytest
import brotli
from src.brotli_compression import compress_data, decompress_data

def test_compress_decompress_data():
    """Test basic compression and decompression."""
    original_data = b"Hello, Brotli compression is awesome!"
    compressed = compress_data(original_data)
    
    # Verify compressed data is bytes and smaller than original
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original_data)
    
    # Test decompression
    decompressed = decompress_data(compressed)
    assert decompressed == original_data

def test_compression_quality():
    """Test different compression qualities."""
    data = b"Test compression quality levels"
    
    # Test various quality levels
    for quality in [0, 5, 11]:
        compressed = compress_data(data, quality=quality)
        decompressed = decompress_data(compressed)
        assert decompressed == data

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        compress_data("Not bytes")
    
    with pytest.raises(TypeError):
        decompress_data("Not bytes")

def test_invalid_compression_quality():
    """Test error handling for invalid compression quality."""
    data = b"Test data"
    
    with pytest.raises(ValueError):
        compress_data(data, quality=-1)
    
    with pytest.raises(ValueError):
        compress_data(data, quality=12)

def test_large_data_compression():
    """Test compression and decompression of larger data."""
    large_data = b"A" * 100000  # 100KB of data
    compressed = compress_data(large_data)
    decompressed = decompress_data(compressed)
    
    assert decompressed == large_data

def test_empty_data_compression():
    """Test compression and decompression of empty data."""
    empty_data = b""
    compressed = compress_data(empty_data)
    decompressed = decompress_data(compressed)
    
    assert decompressed == empty_data