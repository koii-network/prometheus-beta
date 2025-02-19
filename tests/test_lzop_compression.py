import pytest
import lzo
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzop_compression import lzop_compress

def test_lzop_compress_basic():
    """Test basic LZOP compression"""
    input_data = b"Hello, world! This is a test of LZOP compression."
    compressed = lzop_compress(input_data)
    
    # Check basic properties
    assert compressed is not None
    assert len(compressed) > 0
    assert len(compressed) < len(input_data)
    
    # Verify header
    assert compressed[:4] == b'\x4c\x5a\x4f\x50'

def test_lzop_compress_empty_input():
    """Test compression of empty input"""
    input_data = b''
    compressed = lzop_compress(input_data)
    assert compressed == b''

def test_lzop_compress_invalid_input():
    """Test compression with invalid input type"""
    with pytest.raises(ValueError):
        lzop_compress("Not bytes")
    with pytest.raises(ValueError):
        lzop_compress(123)

def test_lzop_compression_decompression():
    """Test that compressed data can be decompressed"""
    input_data = b"Verify compression and decompression functionality"
    compressed = lzop_compress(input_data)
    
    # Extract compressed data (skip header)
    compressed_payload = compressed[12:]
    
    # Decompress and verify
    decompressed = lzo.decompress(compressed_payload)
    assert decompressed == input_data

def test_lzop_compress_large_input():
    """Test compression of larger input"""
    input_data = b"A" * 10000  # Large input
    compressed = lzop_compress(input_data)
    
    assert compressed is not None
    assert len(compressed) > 0
    assert len(compressed) < len(input_data)