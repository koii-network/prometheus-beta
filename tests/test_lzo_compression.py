"""
Tests for LZO Compression Implementation
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzo_compression import lzo_compress, lzo_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression"""
    original_data = b"Hello, world! This is a test of LZO compression."
    compressed = lzo_compress(original_data)
    
    # Compressed data should be different from original
    assert compressed != original_data
    assert len(compressed) <= len(original_data)
    
    # Decompression should restore original data
    decompressed = lzo_decompress(compressed)
    assert decompressed == original_data

def test_repeated_data_compression():
    """Test compression of repeated data"""
    repeated_data = b"ABCABCABCABCABCABC" * 10
    compressed = lzo_compress(repeated_data)
    
    # Compressed data should be significantly smaller
    assert len(compressed) < len(repeated_data)
    
    # Decompression should restore original data
    decompressed = lzo_decompress(compressed)
    assert decompressed == repeated_data

def test_empty_data():
    """Test handling of empty data"""
    with pytest.raises(ValueError):
        lzo_compress(b"")
    
    with pytest.raises(ValueError):
        lzo_decompress(b"")

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        lzo_compress("Not bytes")
    
    with pytest.raises(TypeError):
        lzo_decompress("Not bytes")

def test_large_data_compression():
    """Test compression of larger data"""
    large_data = b"Test data " * 1000
    compressed = lzo_compress(large_data)
    
    # Compressed data should be smaller
    assert len(compressed) < len(large_data)
    
    # Decompression should restore original data
    decompressed = lzo_decompress(compressed)
    assert decompressed == large_data

def test_binary_data_compression():
    """Test compression of binary data"""
    binary_data = bytes(range(256)) * 10
    compressed = lzo_compress(binary_data)
    
    # Decompression should restore original data
    decompressed = lzo_decompress(compressed)
    assert decompressed == binary_data