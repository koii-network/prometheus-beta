import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzo_compression import lzo_compress, lzo_decompress

def test_lzo_compression_decompression():
    """Test basic compression and decompression of data"""
    original_data = b"Hello, World! This is a test of LZO compression."
    compressed = lzo_compress(original_data)
    assert compressed is not None
    assert len(compressed) > 0
    assert compressed != original_data
    
    decompressed = lzo_decompress(compressed)
    assert decompressed == original_data

def test_lzo_compression_string_input():
    """Test compression with string input"""
    original_data = "Hello, World! This is a test of LZO compression."
    compressed = lzo_compress(original_data)
    assert compressed is not None
    
    decompressed = lzo_decompress(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_lzo_compression_empty_input_error():
    """Test error handling for empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzo_compress(b"")
    
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        lzo_decompress(b"")

def test_lzo_compression_none_input_error():
    """Test error handling for None input"""
    with pytest.raises(ValueError, match="Input data cannot be None"):
        lzo_compress(None)
    
    with pytest.raises(ValueError, match="Compressed data cannot be None"):
        lzo_decompress(None)

def test_lzo_compression_invalid_type_error():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        lzo_compress(123)
    
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        lzo_decompress(123)

def test_lzo_compression_large_data():
    """Test compression of larger data"""
    large_data = b"A" * 10000
    compressed = lzo_compress(large_data)
    assert compressed is not None
    assert len(compressed) > 0
    assert len(compressed) < len(large_data)
    
    decompressed = lzo_decompress(compressed)
    assert decompressed == large_data