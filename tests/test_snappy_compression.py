import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from snappy_compression import compress_data, decompress_data

def test_compress_decompress_bytes():
    """Test compression and decompression of byte data"""
    original_data = b'Hello, Snappy compression!'
    compressed = compress_data(original_data)
    assert compressed != original_data
    assert decompress_data(compressed) == original_data

def test_compress_decompress_str():
    """Test compression and decompression of string data"""
    original_data = 'Hello, Snappy compression!'
    compressed = compress_data(original_data)
    assert compressed != original_data.encode('utf-8')
    assert decompress_data(compressed) == original_data.encode('utf-8')

def test_compress_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_data(b'')
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_data('')

def test_compress_none_input():
    """Test handling of None input"""
    with pytest.raises(ValueError, match="Input data cannot be None"):
        compress_data(None)

def test_compress_invalid_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        compress_data(123)
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        compress_data(['list'])

def test_decompress_empty_input():
    """Test handling of empty compressed input"""
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        decompress_data(b'')

def test_decompress_none_input():
    """Test handling of None compressed input"""
    with pytest.raises(ValueError, match="Compressed data cannot be None"):
        decompress_data(None)

def test_decompress_invalid_type():
    """Test handling of invalid compressed input types"""
    with pytest.raises(TypeError, match="Input must be bytes"):
        decompress_data('string')
    with pytest.raises(TypeError, match="Input must be bytes"):
        decompress_data(123)

def test_compress_large_data():
    """Test compression of larger data"""
    large_data = b'A' * 10000
    compressed = compress_data(large_data)
    assert len(compressed) < len(large_data)
    assert decompress_data(compressed) == large_data