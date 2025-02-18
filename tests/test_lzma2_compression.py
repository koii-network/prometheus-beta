import pytest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.lzma2_compression import lzma2_compress, lzma2_decompress

def test_compress_decompress_bytes():
    """Test compression and decompression of byte data"""
    original_data = b'Hello, this is a test of LZMA2 compression!'
    compressed = lzma2_compress(original_data)
    
    # Verify full round trip instead of size
    decompressed = lzma2_decompress(compressed)
    assert decompressed == original_data

def test_compress_decompress_string():
    """Test compression and decompression of string data"""
    original_data = 'Hello, this is a test of LZMA2 compression!'
    compressed = lzma2_compress(original_data)
    
    # Verify full round trip
    decompressed = lzma2_decompress(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_empty_input_raises_error():
    """Test that empty input raises ValueError"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzma2_compress(b'')
    
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzma2_compress('')

def test_invalid_input_type():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        lzma2_compress(123)
    
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        lzma2_decompress('not bytes')

def test_decompress_invalid_data():
    """Test decompressing invalid compressed data"""
    with pytest.raises(ValueError, match="Decompression failed"):
        lzma2_decompress(b'invalid compressed data')

def test_large_data_compression():
    """Test compression of a larger dataset"""
    large_data = b'a' * 10000
    compressed = lzma2_compress(large_data)
    
    # Verify full round trip
    decompressed = lzma2_decompress(compressed)
    assert decompressed == large_data