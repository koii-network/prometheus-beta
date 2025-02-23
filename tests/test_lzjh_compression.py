"""
Test suite for LZJH Compression Algorithm
"""

import pytest
import random
import string
from src.lzjh_compression import lzjh_compress, lzjh_decompress

def test_simple_compression_decompression():
    """Test basic compression and decompression"""
    original = b"HELLO WORLD"
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original

def test_random_data_compression():
    """Test compression with random data"""
    # Generate random bytes
    original = bytes(random.randint(0, 255) for _ in range(1000))
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original

def test_repeated_patterns():
    """Test compression with repeated patterns"""
    original = b"AAAAAAAAAABBBBBBBBBB" * 10
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original

def test_unicode_string():
    """Test compression with unicode string"""
    original = "Hello, 世界! 🌍 How are you?"
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_empty_input_error():
    """Test error handling for empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzjh_compress(b"")
    
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        lzjh_decompress(b"")

def test_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        lzjh_compress(123)
    
    with pytest.raises(TypeError, match="Input must be bytes"):
        lzjh_decompress("not bytes")

def test_malformed_compressed_data():
    """Test error handling for malformed compressed data"""
    with pytest.raises(ValueError, match="Compressed data must have even length"):
        lzjh_decompress(b'\x01')
    
    with pytest.raises(ValueError, match="Compressed data is truncated"):
        lzjh_decompress(b'\x01\x02\x03')

def test_large_random_data():
    """Test compression with larger random data"""
    # Generate a larger random string
    original = ''.join(random.choices(string.ascii_letters + string.digits, k=10000)).encode('utf-8')
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original