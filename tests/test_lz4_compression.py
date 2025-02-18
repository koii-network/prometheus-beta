import pytest
import lz4.frame
from src.lz4_compression import lz4_compress, lz4_decompress

def test_lz4_compression_basic():
    """Test basic compression and decompression"""
    original_data = b"Hello, this is a test string for LZ4 compression!"
    compressed = lz4_compress(original_data)
    assert compressed != original_data
    assert len(compressed) < len(original_data)
    
    decompressed = lz4_decompress(compressed)
    assert decompressed == original_data

def test_lz4_compression_string():
    """Test compression with string input"""
    original_data = "Hello, world! This is a test of string compression."
    compressed = lz4_compress(original_data)
    assert compressed != original_data.encode('utf-8')
    
    decompressed = lz4_decompress(compressed)
    assert decompressed == original_data.encode('utf-8')

def test_lz4_compression_large_data():
    """Test compression with larger data"""
    original_data = b"A" * 10000
    compressed = lz4_compress(original_data)
    assert len(compressed) < len(original_data)
    
    decompressed = lz4_decompress(compressed)
    assert decompressed == original_data

def test_lz4_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        lz4_compress(123)
    
    with pytest.raises(TypeError):
        lz4_decompress(123)

def test_lz4_decompress_invalid_data():
    """Test decompression with invalid compressed data"""
    with pytest.raises(lz4.frame.LZ4FrameError):
        lz4_decompress(b"Invalid compressed data")