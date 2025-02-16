import pytest
import snappy
from src.snappy_compression import snappy_compress, snappy_decompress

def test_snappy_compress_bytes():
    """Test compression of byte data"""
    original_data = b'Hello, this is a test string for Snappy compression!'
    compressed_data = snappy_compress(original_data)
    assert isinstance(compressed_data, bytes)
    assert len(compressed_data) < len(original_data)

def test_snappy_compress_string():
    """Test compression of string data"""
    original_data = 'Hello, this is a test string for Snappy compression!'
    compressed_data = snappy_compress(original_data)
    assert isinstance(compressed_data, bytes)
    assert len(compressed_data) < len(original_data)

def test_snappy_decompress():
    """Test successful decompression"""
    original_data = b'Hello, this is a test string for Snappy compression!'
    compressed_data = snappy_compress(original_data)
    decompressed_data = snappy_decompress(compressed_data)
    assert decompressed_data == original_data

def test_snappy_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        snappy_compress(123)
    
    with pytest.raises(TypeError):
        snappy_decompress(123)

def test_snappy_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError):
        snappy_compress(b'')
    
    with pytest.raises(ValueError):
        snappy_decompress(b'')