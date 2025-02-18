import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzo_compression import compress_lzo, decompress_lzo

def test_compress_decompress_bytes():
    """Test compression and decompression of byte data"""
    original_data = b'Hello, this is a test of LZO compression!'
    compressed = compress_lzo(original_data)
    assert compressed is not None
    assert len(compressed) > 0
    
    decompressed = decompress_lzo(compressed)
    assert decompressed == original_data

def test_compress_decompress_str():
    """Test compression and decompression of string data"""
    original_data = 'Hello, this is a test of LZO compression!'
    compressed = compress_lzo(original_data)
    assert compressed is not None
    assert len(compressed) > 0
    
    # Note: decompression returns bytes, so convert to string for comparison
    decompressed = decompress_lzo(compressed).decode('utf-8')
    assert decompressed == original_data

def test_compress_empty_input():
    """Test compression with empty input raises ValueError"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_lzo(b'')

def test_decompress_empty_input():
    """Test decompression with empty input raises ValueError"""
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        decompress_lzo(b'')

def test_compress_invalid_type():
    """Test compression with invalid input type raises TypeError"""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        compress_lzo(123)

def test_decompress_invalid_type():
    """Test decompression with invalid input type raises TypeError"""
    with pytest.raises(TypeError, match="Input must be bytes"):
        decompress_lzo('not bytes')

def test_large_data_compression():
    """Test compression and decompression of large data"""
    large_data = b'0' * 100000  # 100KB of zeros
    compressed = compress_lzo(large_data)
    assert compressed is not None
    assert len(compressed) > 0
    
    decompressed = decompress_lzo(compressed)
    assert decompressed == large_data