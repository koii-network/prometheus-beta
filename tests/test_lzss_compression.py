"""
Test suite for LZSS Compression Algorithm.

This module contains comprehensive tests for the LZSSCompressor class.
"""

import pytest
import random
from src.lzss_compression import LZSSCompressor

def test_empty_input():
    """Test compression and decompression of empty input."""
    compressor = LZSSCompressor()
    data = b''
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_simple_compression():
    """Test basic compression and decompression."""
    compressor = LZSSCompressor()
    data = b'hello world hello world'
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_repeated_sequence():
    """Test compression of highly repetitive data."""
    compressor = LZSSCompressor()
    data = b'ABCABCABCABCABCABC' * 10
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data
    assert len(compressed) < len(data)

def test_random_data():
    """Test compression of random data."""
    compressor = LZSSCompressor()
    random.seed(42)  # Consistent random data
    data = bytes(random.randint(0, 255) for _ in range(1000))
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_binary_data():
    """Test compression of binary data."""
    compressor = LZSSCompressor()
    data = bytes([0, 1, 255, 0, 1, 255] * 100)
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_long_input():
    """Test compression of a larger input."""
    compressor = LZSSCompressor()
    data = b'Python is awesome! ' * 1000
    compressed = compressor.compress(data)
    decompressed = compressor.decompress(compressed)
    assert decompressed == data

def test_invalid_decompression():
    """Test handling of invalid compressed data."""
    compressor = LZSSCompressor()
    with pytest.raises(ValueError):
        # Invalid flag value
        compressor.decompress(bytes([2, 0, 0]))