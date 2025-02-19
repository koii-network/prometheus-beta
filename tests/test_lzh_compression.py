import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzh_compression import lzh_compress

def test_lzh_compress_empty_input():
    """Test compression of empty input."""
    assert lzh_compress(b'') == b''

def test_lzh_compress_small_input():
    """Test compression of a small input string."""
    input_data = b'Hello, world!'
    compressed = lzh_compress(input_data)
    assert compressed is not None
    assert len(compressed) > 0
    assert len(compressed) <= len(input_data)

def test_lzh_compress_repeated_pattern():
    """Test compression of input with repeated patterns."""
    input_data = b'ABABABABABABABABAB'
    compressed = lzh_compress(input_data)
    assert compressed is not None
    assert len(compressed) > 0
    assert len(compressed) < len(input_data)

def test_lzh_compress_random_bytes():
    """Test compression of random byte sequence."""
    input_data = bytes([i % 256 for i in range(1000)])
    compressed = lzh_compress(input_data)
    assert compressed is not None
    assert len(compressed) > 0

def test_lzh_compress_single_byte():
    """Test compression of a single byte."""
    input_data = b'A'
    compressed = lzh_compress(input_data)
    assert compressed is not None
    assert len(compressed) > 0

def test_lzh_compress_large_input():
    """Test compression of a larger input."""
    input_data = b'This is a test of the LZH compression algorithm. ' * 100
    compressed = lzh_compress(input_data)
    assert compressed is not None
    assert len(compressed) > 0
    assert len(compressed) < len(input_data)