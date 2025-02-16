import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from brotli_compression import compress_brotli, decompress_brotli

def test_brotli_compression_basic():
    """Test basic compression and decompression"""
    original_text = "Hello, Brotli compression!"
    compressed = compress_brotli(original_text)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original_text.encode('utf-8'))
    
    decompressed = decompress_brotli(compressed)
    assert decompressed == original_text

def test_brotli_different_qualities():
    """Test compression with different quality levels"""
    test_text = "Test compression at different quality levels"
    
    # Test various quality levels
    for quality in [0, 5, 11]:
        compressed = compress_brotli(test_text, quality)
        decompressed = decompress_brotli(compressed)
        assert decompressed == test_text

def test_brotli_empty_string():
    """Test compression and decompression of an empty string"""
    original_text = ""
    compressed = compress_brotli(original_text)
    decompressed = decompress_brotli(compressed)
    assert decompressed == original_text

def test_brotli_unicode_text():
    """Test compression with unicode text"""
    original_text = "こんにちは、ブロトリ圧縮！"
    compressed = compress_brotli(original_text)
    decompressed = decompress_brotli(compressed)
    assert decompressed == original_text

def test_brotli_invalid_input_type():
    """Test that invalid input types raise appropriate exceptions"""
    with pytest.raises(TypeError):
        compress_brotli(123)
    
    with pytest.raises(TypeError):
        decompress_brotli("not bytes")

def test_brotli_invalid_quality():
    """Test that invalid compression quality raises ValueError"""
    with pytest.raises(ValueError):
        compress_brotli("test", quality=-1)
    
    with pytest.raises(ValueError):
        compress_brotli("test", quality=12)