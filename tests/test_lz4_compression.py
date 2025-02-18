import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lz4_compression import compress_lz4, decompress_lz4

def test_lz4_compression_and_decompression():
    """Test basic compression and decompression"""
    original_data = b"Hello, this is a test string for LZ4 compression!"
    compressed = compress_lz4(original_data)
    
    # Verify compression creates a non-empty result
    assert len(compressed) > 0
    
    # Verify decompression
    decompressed = decompress_lz4(compressed)
    assert decompressed == original_data

def test_lz4_compression_with_string():
    """Test compression with string input"""
    original_data = "Hello, world! Testing LZ4 compression with string."
    compressed = compress_lz4(original_data)
    
    # Verify compression creates a non-empty result
    assert len(compressed) > 0
    
    # Verify decompression
    decompressed = decompress_lz4(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_lz4_compression_empty_input():
    """Test compression with empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_lz4(b"")
    
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_lz4("")

def test_lz4_compression_none_input():
    """Test compression with None input"""
    with pytest.raises(ValueError, match="Input data cannot be None"):
        compress_lz4(None)

def test_lz4_compression_invalid_type():
    """Test compression with invalid input type"""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        compress_lz4(123)
    
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        compress_lz4(["list", "of", "strings"])

def test_lz4_decompression_invalid_inputs():
    """Test decompression with invalid inputs"""
    with pytest.raises(ValueError, match="Compressed data cannot be None"):
        decompress_lz4(None)
    
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        decompress_lz4(b"")
    
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        decompress_lz4("not bytes")
    
    with pytest.raises(ValueError, match="Decompression failed"):
        decompress_lz4(b"invalid compressed data")