import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from brotli_compression import compress_brotli, decompress_brotli

def test_compress_decompress_str():
    """Test compression and decompression of a string"""
    original_text = "Hello, World! This is a test of Brotli compression."
    compressed = compress_brotli(original_text)
    assert compressed is not None
    assert len(compressed) < len(original_text.encode('utf-8'))
    
    decompressed = decompress_brotli(compressed)
    assert decompressed.decode('utf-8') == original_text

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes"""
    original_bytes = b"Binary data for compression test"
    compressed = compress_brotli(original_bytes)
    assert compressed is not None
    assert len(compressed) < len(original_bytes)
    
    decompressed = decompress_brotli(compressed)
    assert decompressed == original_bytes

def test_compression_quality():
    """Test different compression qualities"""
    text = "Test compression quality variations"
    
    # Test lowest quality
    compressed_low = compress_brotli(text, quality=0)
    decompressed_low = decompress_brotli(compressed_low)
    assert decompressed_low.decode('utf-8') == text
    
    # Test highest quality
    compressed_high = compress_brotli(text, quality=11)
    decompressed_high = decompress_brotli(compressed_high)
    assert decompressed_high.decode('utf-8') == text

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compress_brotli(123)
    
    with pytest.raises(TypeError):
        decompress_brotli("not bytes")

def test_invalid_compression_quality():
    """Test error handling for invalid compression quality"""
    with pytest.raises(ValueError):
        compress_brotli("test", quality=-1)
    
    with pytest.raises(ValueError):
        compress_brotli("test", quality=12)

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_str = ""
    empty_bytes = b""
    
    compressed_str = compress_brotli(empty_str)
    assert decompress_brotli(compressed_str).decode('utf-8') == empty_str
    
    compressed_bytes = compress_brotli(empty_bytes)
    assert decompress_brotli(compressed_bytes) == empty_bytes