import pytest
import lzma
from src.lzma2_compression import lzma2_compress, lzma2_decompress

def test_lzma2_compression_basic():
    """Test basic compression and decompression of a string"""
    original_data = "Hello, world! This is a test of LZMA2 compression."
    compressed = lzma2_compress(original_data)
    
    # Verify round-trip compression works
    decompressed = lzma2_decompress(compressed)
    assert decompressed.decode('utf-8') == original_data

def test_lzma2_compression_bytes():
    """Test compression and decompression of bytes"""
    original_data = b'\x00\x01\x02\x03\x04\x05'
    compressed = lzma2_compress(original_data)
    
    # Verify round-trip compression works
    decompressed = lzma2_decompress(compressed)
    assert decompressed == original_data

def test_lzma2_compression_empty_input():
    """Test error handling for empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzma2_compress("")
    
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        lzma2_decompress(b'')

def test_lzma2_compression_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        lzma2_compress(123)
    
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        lzma2_decompress("not bytes")

def test_lzma2_compression_large_data():
    """Test compression and decompression of larger data"""
    large_data = "x" * 10000  # 10,000 characters
    compressed = lzma2_compress(large_data)
    
    # Verify round-trip compression
    decompressed = lzma2_decompress(compressed)
    assert decompressed.decode('utf-8') == large_data