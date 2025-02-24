import pytest
import random
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzop_compression import lzop_compress, lzop_decompress

def test_lzop_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, LZOP compression!"
    compressed = lzop_compress(original_data)
    decompressed = lzop_decompress(compressed)
    
    assert decompressed == original_data

def test_lzop_compression_large_data():
    """Test compression with larger random data"""
    # Generate 100KB of random data
    random.seed(42)  # For reproducibility
    original_data = bytes(random.getrandbits(8) for _ in range(100 * 1024))
    
    compressed = lzop_compress(original_data)
    decompressed = lzop_decompress(compressed)
    
    assert decompressed == original_data

def test_lzop_compression_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzop_compress(b"")

def test_lzop_decompression_invalid_input():
    """Test handling of invalid input for decompression"""
    # Test too short input
    with pytest.raises(ValueError, match="Invalid LZOP data"):
        lzop_decompress(b"short")
    
    # Test invalid magic number
    with pytest.raises(ValueError, match="Invalid LZOP magic number"):
        lzop_decompress(b"FAKE" + b"\x00" * 10)

def test_lzop_compression_invalid_type():
    """Test handling of non-bytes input"""
    with pytest.raises(ValueError, match="Input must be bytes"):
        lzop_compress("Not bytes")
    
    with pytest.raises(ValueError, match="Input must be bytes"):
        lzop_decompress("Not bytes")

def test_lzop_compression_compressibility():
    """Test that compression reduces data size"""
    # Create a repetitive data pattern
    original_data = b"REPEAT_THIS_DATA_MULTIPLE_TIMES" * 1000
    
    compressed = lzop_compress(original_data)
    
    # Compressed data should be smaller than original
    assert len(compressed) < len(original_data)
    
    # Decompression should restore original data
    decompressed = lzop_decompress(compressed)
    assert decompressed == original_data