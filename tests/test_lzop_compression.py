import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzop_compression import lzop_compress, lzop_decompress

def test_lzop_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, LZOP compression!"
    compressed_data = lzop_compress(original_data)
    assert compressed_data is not None
    assert len(compressed_data) > 0
    assert len(compressed_data) < len(original_data)

def test_lzop_compression_symmetric():
    """Test that decompression recovers the original data"""
    original_data = b"Hello, LZOP compression!"
    compressed_data = lzop_compress(original_data)
    decompressed_data = lzop_decompress(compressed_data)
    assert decompressed_data == original_data

def test_lzop_compression_empty_data():
    """Test compression with empty data"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzop_compress(b"")

def test_lzop_decompression_invalid_data():
    """Test decompression with invalid data"""
    with pytest.raises(ValueError, match="Invalid LZOP magic number"):
        lzop_decompress(b"INVALID_DATA")

def test_lzop_compression_input_type():
    """Test compression with invalid input type"""
    with pytest.raises(TypeError, match="Input must be bytes"):
        lzop_compress("Not bytes")

def test_lzop_decompression_input_type():
    """Test decompression with invalid input type"""
    with pytest.raises(TypeError, match="Input must be bytes"):
        lzop_decompress("Not bytes")

def test_lzop_compression_large_data():
    """Test compression with larger data"""
    original_data = b"x" * 10000  # Large data
    compressed_data = lzop_compress(original_data)
    decompressed_data = lzop_decompress(compressed_data)
    assert decompressed_data == original_data