import pytest
import snappy
from src.snappy_compression import compress_data, decompress_data

def test_compression_decompression():
    """Test basic compression and decompression"""
    original_data = b"Hello, Snappy compression!"
    compressed = compress_data(original_data)
    assert compressed != original_data
    assert len(compressed) < len(original_data)
    
    # Verify decompression works
    decompressed = decompress_data(compressed)
    assert decompressed == original_data

def test_string_input():
    """Test compression with string input"""
    original_data = "Hello, Snappy compression!"
    compressed = compress_data(original_data)
    
    # Verify decompression works with string input
    decompressed = decompress_data(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_empty_input_raises_error():
    """Test that empty input raises ValueError"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_data(b"")
    
    with pytest.raises(ValueError, match="Input compressed data cannot be empty"):
        decompress_data(b"")

def test_invalid_input_type():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        compress_data(123)
    
    with pytest.raises(TypeError, match="Input must be bytes"):
        decompress_data(123)

def test_large_data_compression():
    """Test compression with larger data"""
    large_data = b"A" * 10000
    compressed = compress_data(large_data)
    assert len(compressed) < len(large_data)
    
    decompressed = decompress_data(compressed)
    assert decompressed == large_data

def test_multiple_compression_decompression():
    """Test multiple rounds of compression and decompression"""
    data = b"Repeated compression test"
    for _ in range(5):
        compressed = compress_data(data)
        data = decompress_data(compressed)