import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzo_compression import lzo_compress, lzo_decompress

def test_lzo_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, this is a test of LZO compression!"
    compressed = lzo_compress(original_data)
    assert compressed is not None
    assert len(compressed) > 0
    assert compressed != original_data

def test_lzo_compression_decompression():
    """Test that compressed data can be decompressed back to original"""
    original_data = b"Hello, this is a test of LZO compression!"
    compressed = lzo_compress(original_data)
    decompressed = lzo_decompress(compressed)
    assert decompressed == original_data

def test_lzo_empty_input():
    """Test compression and decompression of empty input"""
    empty_data = b''
    compressed = lzo_compress(empty_data)
    assert compressed == b''
    decompressed = lzo_decompress(compressed)
    assert decompressed == b''

def test_lzo_invalid_input_type():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        lzo_compress("not bytes")
    with pytest.raises(TypeError):
        lzo_decompress("not bytes")

def test_lzo_large_data():
    """Test compression and decompression of larger data"""
    large_data = b"a" * 10000
    compressed = lzo_compress(large_data)
    assert compressed is not None
    assert len(compressed) > 0
    decompressed = lzo_decompress(compressed)
    assert decompressed == large_data