import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data

def test_compress_decompress_string():
    """Test compression and decompression of a string."""
    original_data = "Hello, world! This is a test of Zlib compression."
    compressed = compress_data(original_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original_data.encode('utf-8'))
    
    decompressed = decompress_data(compressed)
    assert decompressed.decode('utf-8') == original_data

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes."""
    original_data = b"Binary data compression test"
    compressed = compress_data(original_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original_data)
    
    decompressed = decompress_data(compressed)
    assert decompressed == original_data

def test_different_compression_levels():
    """Test different compression levels."""
    data = "Compression level test" * 100  # Repeated data for better compression
    
    # Test different compression levels
    levels = [0, 3, 6, 9]
    compressed_sizes = []
    
    for level in levels:
        compressed = compress_data(data, level)
        compressed_sizes.append(len(compressed))
        
        # Verify decompression works
        decompressed = decompress_data(compressed)
        assert decompressed.decode('utf-8') == data
    
    # Higher compression levels should generally result in smaller compressed sizes
    assert compressed_sizes[0] >= compressed_sizes[-1]

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data("not bytes")

def test_invalid_compression_level():
    """Test error handling for invalid compression levels."""
    with pytest.raises(ValueError):
        compress_data("test", -1)
    
    with pytest.raises(ValueError):
        compress_data("test", 10)

def test_decompress_invalid_data():
    """Test decompression of invalid compressed data."""
    with pytest.raises(zlib.error):
        decompress_data(b"Invalid compressed data")

def test_empty_input():
    """Test compression and decompression of empty input."""
    empty_string = ""
    empty_bytes = b""
    
    # String test
    compressed_str = compress_data(empty_string)
    assert decompress_data(compressed_str).decode('utf-8') == empty_string
    
    # Bytes test
    compressed_bytes = compress_data(empty_bytes)
    assert decompress_data(compressed_bytes) == empty_bytes