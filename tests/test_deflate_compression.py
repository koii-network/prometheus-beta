import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from deflate_compression import deflate_compress, deflate_decompress

def test_compression_decompression():
    """Test basic compression and decompression"""
    original_data = b"Hello, this is a test string for Deflate compression!"
    compressed = deflate_compress(original_data)
    
    # Verify compression reduces size
    assert len(compressed) < len(original_data)
    
    # Verify round-trip compression/decompression
    decompressed = deflate_decompress(compressed)
    assert decompressed == original_data

def test_string_input():
    """Test compression with string input"""
    original_data = "Hello, world!"
    compressed = deflate_compress(original_data)
    decompressed = deflate_decompress(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_empty_input_compression():
    """Test compression with empty input raises ValueError"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        deflate_compress(b"")
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        deflate_compress("")

def test_empty_input_decompression():
    """Test decompression with empty input raises ValueError"""
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        deflate_decompress(b"")

def test_invalid_input_type_compression():
    """Test compression with invalid input type raises TypeError"""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        deflate_compress(123)
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        deflate_compress(["list"])

def test_invalid_input_type_decompression():
    """Test decompression with invalid input type raises TypeError"""
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        deflate_decompress("string")
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        deflate_decompress(123)

def test_large_data_compression():
    """Test compression with larger data"""
    large_data = b"x" * 10000  # 10KB of repeated data
    compressed = deflate_compress(large_data)
    
    # Verify compression significantly reduces size for repetitive data
    assert len(compressed) < len(large_data)
    
    decompressed = deflate_decompress(compressed)
    assert decompressed == large_data

def test_invalid_compressed_data():
    """Test decompression with invalid compressed data"""
    with pytest.raises(RuntimeError, match="Decompression failed"):
        deflate_decompress(b"invalid compressed data")