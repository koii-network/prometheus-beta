import pytest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.snappy_compression import snappy_compress, snappy_decompress

def test_compress_decompress_bytes():
    """Test compression and decompression of byte data."""
    original_data = b'Hello, Snappy compression!'
    compressed = snappy_compress(original_data)
    assert compressed != original_data
    assert len(compressed) < len(original_data)
    
    decompressed = snappy_decompress(compressed)
    assert decompressed == original_data

def test_compress_decompress_str():
    """Test compression and decompression of string data."""
    original_data = 'Hello, Snappy compression!'
    compressed = snappy_compress(original_data)
    assert compressed != original_data.encode('utf-8')
    
    decompressed = snappy_decompress(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_empty_input_errors():
    """Test error handling for empty inputs."""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        snappy_compress(b'')
    
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        snappy_decompress(b'')

def test_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        snappy_compress(123)
    
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        snappy_decompress(123)

def test_large_data_compression():
    """Test compression of large data."""
    large_data = b'A' * 10000
    compressed = snappy_compress(large_data)
    assert len(compressed) < len(large_data)
    
    decompressed = snappy_decompress(compressed)
    assert decompressed == large_data