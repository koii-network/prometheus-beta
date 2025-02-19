import pytest
from src.lzp_compression import lzp_compress, lzp_decompress

def test_lzp_compression_basic():
    """Test basic compression and decompression"""
    original = "hello world"
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_compression_empty_string():
    """Test compression and decompression of empty string"""
    original = ""
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_compression_repeated_pattern():
    """Test compression of text with repeated patterns"""
    original = "ababababab"
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_compression_long_text():
    """Test compression of a longer text"""
    original = "The quick brown fox jumps over the lazy dog. " * 10
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_compression_special_characters():
    """Test compression with special characters and mixed content"""
    original = "Hello, World! 123 @#$ Testing 🚀"
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_compression_ratio():
    """Verify that compression produces a list of indices"""
    original = "hello world"
    compressed = lzp_compress(original)
    assert isinstance(compressed, list)
    assert all(isinstance(x, int) for x in compressed)