import pytest
from src.lzw_compression import lzw_compress, lzw_decompress

def test_lzw_compression_basic():
    """Test basic compression and decompression"""
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_compression_empty_string():
    """Test compression and decompression of empty string"""
    original = ""
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_compression_single_char():
    """Test compression and decompression of single character"""
    original = "A"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_compression_repeated_chars():
    """Test compression of repeated characters"""
    original = "AAAAAAAA"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_compression_mixed_chars():
    """Test compression of mixed characters"""
    original = "abcabcabcabc"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_compression_with_special_chars():
    """Test compression with special characters"""
    original = "Hello, World! 123"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_compression_unicode():
    """Test compression with unicode characters"""
    original = "こんにちは世界"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original