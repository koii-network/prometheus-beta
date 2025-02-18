import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzo_compression import compress_lzo, decompress_lzo

def test_lzo_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, LZO compression!"
    compressed = compress_lzo(original_data)
    decompressed = decompress_lzo(compressed)
    
    assert decompressed == original_data

def test_lzo_compression_empty_input():
    """Test that empty input raises a ValueError"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_lzo(b"")

def test_lzo_compression_type_error():
    """Test that non-bytes input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be bytes"):
        compress_lzo("Not bytes")

def test_lzo_decompression_type_error():
    """Test that non-bytes input for decompression raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be bytes"):
        decompress_lzo("Not bytes")

def test_lzo_decompression_short_input():
    """Test that too short input for decompression raises a ValueError"""
    with pytest.raises(ValueError, match="Compressed data is too short"):
        decompress_lzo(b"123")

def test_lzo_compression_large_data():
    """Test compression and decompression of larger data"""
    original_data = b"0" * 10000  # Large input
    compressed = compress_lzo(original_data)
    decompressed = decompress_lzo(compressed)
    
    assert decompressed == original_data