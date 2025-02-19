import pytest
from src.lzp_compression import lzp_compress, lzp_decompress

def test_lzp_compression_basic():
    """Test basic compression and decompression"""
    original = b"hello world"
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_compression_empty_input():
    """Test compression and decompression of empty input"""
    original = b""
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_compression_repeated_data():
    """Test compression of highly repetitive data"""
    original = b"aaaaaaaaaabbbbbbbbbb"
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_compression_mixed_data():
    """Test compression of mixed data types"""
    original = b"hello123world456"
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_compression_string_input():
    """Test compression with string input"""
    original = "hello world"
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_compression_ratio():
    """Verify that compression reduces data size"""
    original = b"hello world" * 100  # Repetitive data
    compressed = lzp_compress(original)
    assert len(compressed) < len(original)