import pytest
import sys
import os

# Ensure src directory is in Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from snappy_compression import snappy_compress, snappy_decompress

def test_snappy_compression_basic():
    """Test basic compression and decompression of string"""
    original_data = "Hello, Snappy compression!"
    compressed = snappy_compress(original_data)
    
    # Verify compression reduces size
    assert len(compressed) < len(original_data.encode('utf-8'))
    
    # Verify decompression works
    decompressed = snappy_decompress(compressed)
    assert decompressed.decode('utf-8') == original_data

def test_snappy_compression_bytes():
    """Test compression and decompression of bytes"""
    original_data = b'\x00\x01\x02\x03\x04'
    compressed = snappy_compress(original_data)
    
    # Verify compression reduces size
    assert len(compressed) <= len(original_data)
    
    # Verify decompression works
    decompressed = snappy_decompress(compressed)
    assert decompressed == original_data

def test_snappy_compress_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        snappy_compress(123)
    
    with pytest.raises(TypeError):
        snappy_compress(None)
    
    with pytest.raises(ValueError):
        snappy_compress(b'')

def test_snappy_decompress_invalid_input():
    """Test error handling for invalid decompress inputs"""
    with pytest.raises(TypeError):
        snappy_decompress("not bytes")
    
    with pytest.raises(ValueError):
        snappy_decompress(b'')