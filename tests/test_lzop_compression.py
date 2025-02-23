import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzop_compression import lzop_compress, lzop_decompress

def test_compression_decompression():
    """Test basic compression and decompression"""
    original_data = b"Hello, this is a test of LZOP-like compression!"
    compressed = lzop_compress(original_data)
    
    # Compressed data should be different from original
    assert compressed != original_data
    
    # Decompression should return original data
    decompressed = lzop_decompress(compressed)
    assert decompressed == original_data

def test_large_data_compression():
    """Test compression with larger data"""
    original_data = b"A" * 10000
    compressed = lzop_compress(original_data)
    decompressed = lzop_decompress(compressed)
    assert decompressed == original_data

def test_empty_data_raises_error():
    """Test that empty data raises a ValueError"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzop_compress(b"")

def test_invalid_input_type():
    """Test that non-bytes input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be bytes"):
        lzop_compress("Not bytes")
    
    with pytest.raises(TypeError, match="Input must be bytes"):
        lzop_decompress("Not bytes")

def test_invalid_compressed_data():
    """Test error handling for invalid compressed data"""
    # Too short compressed data
    with pytest.raises(ValueError, match="Compressed data is too short"):
        lzop_decompress(b"short")
    
    # Corrupted compressed data (with invalid version)
    with pytest.raises(ValueError, match="Unsupported compression version"):
        malformed_data = struct.pack('>IIHH', 100, 50, 999, 0) + b"some compressed data"
        lzop_decompress(malformed_data)

def test_random_binary_data():
    """Test compression with random binary data"""
    import os
    random_data = os.urandom(1024)
    compressed = lzop_compress(random_data)
    decompressed = lzop_decompress(compressed)
    assert decompressed == random_data