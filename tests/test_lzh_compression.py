import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzh_compression import lzh_compress

def test_lzh_compress_basic_string():
    """Test basic string compression"""
    input_data = "ABRACADABRA"
    compressed = lzh_compress(input_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0

def test_lzh_compress_bytes():
    """Test bytes compression"""
    input_data = b'Hello, world!'
    compressed = lzh_compress(input_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0

def test_lzh_compress_empty_input():
    """Test error handling for empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzh_compress("")
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzh_compress(b'')

def test_lzh_compress_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be str or bytes"):
        lzh_compress(123)
    with pytest.raises(TypeError, match="Input must be str or bytes"):
        lzh_compress(None)

def test_lzh_compress_repeated_pattern():
    """Test compression of input with repeated patterns"""
    input_data = "AAAAAAAAAAA"
    compressed = lzh_compress(input_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0

def test_lzh_compress_unicode_string():
    """Test compression of unicode string"""
    input_data = "こんにちは世界"
    compressed = lzh_compress(input_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0