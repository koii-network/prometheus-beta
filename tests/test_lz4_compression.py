"""
Tests for LZ4 Compression Implementation
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lz4_compression import lz4_compress, lz4_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression of a simple string"""
    original = "Hello, world! This is a test of LZ4 compression."
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed.decode('utf-8') == original

def test_repeated_data_compression():
    """Test compression of data with repeated patterns"""
    original = "AAAAAAAAAABBBBBBBBBBCCCCCCCCCC" * 10
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed.decode('utf-8') == original

def test_binary_data_compression():
    """Test compression of binary data"""
    original = bytes([1, 2, 3, 4, 5, 1, 2, 3, 4, 5] * 10)
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed == original

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError"""
    with pytest.raises(ValueError):
        lz4_compress("")
    
    with pytest.raises(ValueError):
        lz4_decompress(b"")

def test_invalid_input_type():
    """Test that invalid input types raise TypeError"""
    with pytest.raises(TypeError):
        lz4_compress(123)
    
    with pytest.raises(TypeError):
        lz4_decompress(123)

def test_random_data_compression():
    """Test compression and decompression of random data"""
    import random
    
    # Generate a random byte string
    random.seed(42)  # For reproducibility
    original = bytes(random.getrandbits(8) for _ in range(1000))
    
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed == original

def test_various_string_inputs():
    """Test compression with various string inputs"""
    test_cases = [
        "Short string",
        "Repeated pattern " * 5,
        "123456789" * 10,
        "!@#$%^&*()" * 3
    ]
    
    for test_input in test_cases:
        compressed = lz4_compress(test_input)
        decompressed = lz4_decompress(compressed)
        assert decompressed.decode('utf-8') == test_input

def test_unicode_string_compression():
    """Test compression of unicode strings"""
    original = "こんにちは世界 Hello World 🌍 múltiple languages"
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed.decode('utf-8') == original