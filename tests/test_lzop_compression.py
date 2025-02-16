import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzop_compression import lzop_compress, lzop_decompress

def test_lzop_compression_decompression():
    """
    Test basic compression and decompression functionality
    """
    original_data = b"Hello, this is a test string for LZOP compression!"
    
    # Compress the data
    compressed_data = lzop_compress(original_data)
    
    # Verify compression reduced data size
    assert len(compressed_data) < len(original_data)
    
    # Decompress the data
    decompressed_data = lzop_decompress(compressed_data)
    
    # Verify decompressed data matches original
    assert decompressed_data == original_data

def test_compression_edge_cases():
    """
    Test edge cases and error handling
    """
    # Test empty input
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzop_compress(b"")
    
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        lzop_decompress(b"")
    
    # Test invalid input type
    with pytest.raises(TypeError, match="Input must be bytes"):
        lzop_compress("Not bytes")
    
    with pytest.raises(TypeError, match="Input must be bytes"):
        lzop_decompress("Not bytes")

def test_large_data_compression():
    """
    Test compression and decompression with larger data
    """
    # Create a larger test string
    large_data = b"This is a much larger test string " * 1000
    
    # Compress the data
    compressed_data = lzop_compress(large_data)
    
    # Verify compression reduced data size
    assert len(compressed_data) < len(large_data)
    
    # Decompress the data
    decompressed_data = lzop_decompress(compressed_data)
    
    # Verify decompressed data matches original
    assert decompressed_data == large_data