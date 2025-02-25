import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzh_compression import LZHCompressor

def test_lzh_compressor_basic_compression():
    """Test basic compression of a simple string"""
    original = "HELLO WORLD"
    compressed = LZHCompressor.compress(original)
    assert compressed is not None
    assert len(compressed) > 0
    assert compressed != original.encode('utf-8')

def test_lzh_compressor_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        LZHCompressor.compress("")

def test_lzh_compressor_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError, match="Input must be string or bytes"):
        LZHCompressor.compress(12345)

def test_lzh_compressor_bytes_input():
    """Test compression with bytes input"""
    original = b"HELLO WORLD"
    compressed = LZHCompressor.compress(original)
    assert compressed is not None
    assert len(compressed) > 0

def test_lzh_compressor_repeated_patterns():
    """Test compression of input with repeated patterns"""
    original = "AAAAAAAAAA"
    compressed = LZHCompressor.compress(original)
    assert compressed is not None
    assert len(compressed) > 0
    assert len(compressed) < len(original)

def test_lzh_decompressor_empty_input():
    """Test handling of empty input in decompression"""
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        LZHCompressor.decompress(b"")

def test_lzh_decompressor_invalid_input_type():
    """Test handling of invalid input types in decompression"""
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        LZHCompressor.decompress("not bytes")

def test_lzh_compression_length_preservation():
    """Verify that compression doesn't lose data completely"""
    original = "This is a test string with some repeated content"
    compressed = LZHCompressor.compress(original)
    assert len(compressed) > 0
    assert len(compressed) < len(original.encode('utf-8'))

def test_lzh_compressor_unicode_input():
    """Test compression with unicode characters"""
    original = "Hello, 世界! こんにちは"
    compressed = LZHCompressor.compress(original)
    assert compressed is not None
    assert len(compressed) > 0