import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from snappy_compression import compress_data, decompress_data

def test_compress_decompress_bytes():
    """Test compression and decompression of byte data"""
    original_data = b"Hello, Snappy compression!"
    compressed = compress_data(original_data)
    decompressed = decompress_data(compressed)
    
    assert original_data == decompressed
    assert len(compressed) < len(original_data)

def test_compress_decompress_str():
    """Test compression and decompression of string data"""
    original_data = "Hello, Snappy compression!"
    compressed = compress_data(original_data)
    decompressed = decompress_data(compressed)
    
    assert original_data.encode('utf-8') == decompressed
    assert len(compressed) < len(original_data)

def test_large_data_compression():
    """Test compression and decompression of large data"""
    original_data = b"a" * 10000
    compressed = compress_data(original_data)
    decompressed = decompress_data(compressed)
    
    assert original_data == decompressed
    assert len(compressed) < len(original_data)

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data(123)

def test_none_input():
    """Test handling of None input"""
    with pytest.raises(ValueError):
        compress_data(None)
    
    with pytest.raises(ValueError):
        decompress_data(None)

def test_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError):
        compress_data(b"")
    
    with pytest.raises(ValueError):
        decompress_data(b"")