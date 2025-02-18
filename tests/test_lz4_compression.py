import pytest
from src.lz4_compression import lz4_compress, lz4_decompress

def test_lz4_compression_basic():
    """Test basic compression and decompression of a simple string"""
    original = "hello world"
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz4_compression_repeated_data():
    """Test compression of data with repeated sequences"""
    original = "abcabcabcabc" * 10
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz4_compression_bytes():
    """Test compression of raw bytes"""
    original = b'\x00\x01\x02\x03\x00\x01\x02\x03'
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    assert decompressed == original

def test_lz4_compression_empty_data():
    """Test compression of empty data"""
    original = ""
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz4_compression_error_handling():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        lz4_compress(123)
    
    with pytest.raises(TypeError):
        lz4_decompress(123)

def test_lz4_compression_large_data():
    """Test compression of larger data"""
    original = "test data " * 1000
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_lz4_compression_unicode():
    """Test compression of unicode strings"""
    original = "こんにちは世界" * 5
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    assert decompressed.decode('utf-8') == original