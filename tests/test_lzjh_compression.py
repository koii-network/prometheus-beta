import pytest
from src.lzjh_compression import lzjh_compress, lzjh_decompress

def test_lzjh_compression_basic():
    """Test basic compression and decompression"""
    original = b"HELLO WORLD HELLO WORLD"
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    
    assert decompressed == original

def test_lzjh_compression_repeat_patterns():
    """Test compression with repeated patterns"""
    original = b"ABCABCABCABC" * 10
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    
    assert decompressed == original

def test_lzjh_compression_empty_input():
    """Test compression with empty input"""
    original = b""
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    
    assert decompressed == original

def test_lzjh_compression_string_input():
    """Test compression with string input"""
    original = "Hello, World! Repeated text for better compression."
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    
    assert decompressed == original.encode('utf-8')

def test_lzjh_compression_random_bytes():
    """Test compression with random bytes"""
    import random
    original = bytes(random.randint(0, 255) for _ in range(1000))
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    
    assert decompressed == original