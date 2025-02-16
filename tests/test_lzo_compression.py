import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzo_compression import lzo_compress, lzo_decompress

def test_lzo_compression_decompression():
    """Test basic compression and decompression"""
    original_data = b"Hello, this is a test of LZO compression!"
    compressed = lzo_compress(original_data)
    decompressed = lzo_decompress(compressed)
    
    assert decompressed == original_data

def test_lzo_compression_with_string():
    """Test compression works with string input"""
    original_data = "Hello, world!"
    compressed = lzo_compress(original_data)
    decompressed = lzo_decompress(compressed)
    
    assert decompressed == original_data.encode('utf-8')

def test_lzo_empty_input_raises_error():
    """Test that empty input raises a ValueError"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzo_compress(b"")

def test_lzo_invalid_input_type():
    """Test that invalid input types raise a TypeError"""
    with pytest.raises(TypeError):
        lzo_compress(123)
    with pytest.raises(TypeError):
        lzo_decompress(123)

def test_lzo_compression_large_data():
    """Test compression with larger data"""
    original_data = b"A" * 10000
    compressed = lzo_compress(original_data)
    decompressed = lzo_decompress(compressed)
    
    assert decompressed == original_data

def test_lzo_decompress_invalid_data():
    """Test that invalid compressed data raises an error"""
    with pytest.raises(ValueError, match="Invalid compressed data"):
        lzo_decompress(b"short")