import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzop_compression import lzop_compress, lzop_decompress

def test_compression_decompression():
    """Test basic compression and decompression"""
    original_data = b"Hello, this is a test of LZOP compression algorithm!"
    
    # Compress
    compressed = lzop_compress(original_data)
    assert compressed is not None
    assert len(compressed) > 0
    assert len(compressed) < len(original_data)
    
    # Decompress
    decompressed = lzop_decompress(compressed)
    assert decompressed == original_data

def test_empty_data():
    """Test compression and decompression of empty data"""
    empty_data = b""
    
    # Compress
    compressed = lzop_compress(empty_data)
    assert compressed == b''
    
    # Decompress
    decompressed = lzop_decompress(compressed)
    assert decompressed == b''

def test_large_data():
    """Test compression and decompression of larger data"""
    large_data = b"Hello " * 1000
    
    # Compress
    compressed = lzop_compress(large_data)
    assert compressed is not None
    assert len(compressed) > 0
    assert len(compressed) < len(large_data)
    
    # Decompress
    decompressed = lzop_decompress(compressed)
    assert decompressed == large_data

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        lzop_compress("Not bytes")
    
    with pytest.raises(TypeError):
        lzop_decompress("Not bytes")

def test_corrupted_data():
    """Test handling of corrupted compressed data"""
    original_data = b"Hello, test data!"
    compressed = lzop_compress(original_data)
    
    # Corrupt the compressed data
    corrupted_data = compressed[:10] + b'\x00\x00' + compressed[12:]
    
    with pytest.raises(ValueError):
        lzop_decompress(corrupted_data)