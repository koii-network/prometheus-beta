"""
Test suite for LZVN compression algorithm implementation.
"""

import pytest
from src.lzvn_compression import lzvn_compress, lzvn_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression of simple data."""
    original_data = b"Hello, world! This is a test of LZVN compression."
    compressed = lzvn_compress(original_data)
    assert compressed != original_data
    assert len(compressed) < len(original_data)
    
    decompressed = lzvn_decompress(compressed)
    assert decompressed == original_data

def test_repeated_data_compression():
    """Test compression of data with repeated patterns."""
    original_data = b"ABCABCABCABCABCABCABCABC" * 10
    compressed = lzvn_compress(original_data)
    assert len(compressed) < len(original_data)
    
    decompressed = lzvn_decompress(compressed)
    assert decompressed == original_data

def test_empty_input():
    """Test handling of empty input."""
    with pytest.raises(ValueError):
        lzvn_compress(b"")
    
    with pytest.raises(ValueError):
        lzvn_decompress(b"")

def test_invalid_input_type():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        lzvn_compress("Not bytes")
    
    with pytest.raises(TypeError):
        lzvn_decompress("Not bytes")

def test_binary_data_compression():
    """Test compression of binary data."""
    original_data = bytes([
        0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5,
        255, 254, 253, 252, 255, 254, 253, 252
    ] * 5)
    compressed = lzvn_compress(original_data)
    assert len(compressed) < len(original_data)
    
    decompressed = lzvn_decompress(compressed)
    assert decompressed == original_data

def test_large_data_compression():
    """Test compression of larger data set."""
    original_data = bytes(range(256)) * 100  # Repeat byte sequence
    compressed = lzvn_compress(original_data)
    assert len(compressed) < len(original_data)
    
    decompressed = lzvn_decompress(compressed)
    assert decompressed == original_data