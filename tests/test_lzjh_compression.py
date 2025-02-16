import pytest
from src.lzjh_compression import lzjh_compress, lzjh_decompress

def test_lzjh_compression_basic():
    """Test basic compression and decompression"""
    original = b"ABRACADABRA"
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original

def test_lzjh_compression_repeated_pattern():
    """Test compression of repeated patterns"""
    original = b"AAAAAAAAAAAAAA"
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original

def test_lzjh_compression_string_input():
    """Test compression with string input"""
    original = "Hello, world!"
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original.encode('utf-8')

def test_lzjh_compression_empty_input():
    """Test compression of empty input"""
    original = b""
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original

def test_lzjh_compression_invalid_input_type():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        lzjh_compress(123)
    
    with pytest.raises(TypeError):
        lzjh_decompress(123)

def test_lzjh_compression_large_input():
    """Test compression of a larger input"""
    original = b"Hello " * 1000
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original