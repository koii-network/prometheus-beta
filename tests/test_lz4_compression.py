import pytest
import lz4.frame
from src.lz4_compression import compress_lz4, decompress_lz4

def test_lz4_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, world! This is a test of LZ4 compression."
    compressed = compress_lz4(original_data)
    assert compressed != original_data  # Compressed data should be different
    assert len(compressed) < len(original_data)  # Compressed data should be smaller or equal
    
    decompressed = decompress_lz4(compressed)
    assert decompressed == original_data  # Decompressed data should match original

def test_lz4_compression_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compress_lz4(b"")
    
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        decompress_lz4(b"")

def test_lz4_compression_invalid_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError, match="Input must be bytes"):
        compress_lz4("not bytes")
    
    with pytest.raises(TypeError, match="Input must be bytes"):
        decompress_lz4("not bytes")

def test_lz4_compression_large_data():
    """Test compression of larger data"""
    large_data = b"A" * 10000  # 10,000 bytes of repeated 'A'
    compressed = compress_lz4(large_data)
    assert compressed != large_data
    
    decompressed = decompress_lz4(compressed)
    assert decompressed == large_data

def test_lz4_compression_random_data():
    """Test compression of random data"""
    import os
    random_data = os.urandom(1000)  # 1000 bytes of random data
    compressed = compress_lz4(random_data)
    
    decompressed = decompress_lz4(compressed)
    assert decompressed == random_data