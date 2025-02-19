import pytest
import zlib
from src.deflate_compression import deflate_compress, deflate_decompress

def test_compress_decompress_text():
    """Test compression and decompression of a text string"""
    original_text = "Hello, world! This is a test of Deflate compression."
    compressed = deflate_compress(original_text)
    assert compressed != original_text.encode('utf-8')
    
    decompressed = deflate_decompress(compressed)
    assert decompressed.decode('utf-8') == original_text

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes"""
    original_bytes = b'\x00\x01\x02\x03\x04\x05\x06\x07'
    compressed = deflate_compress(original_bytes)
    assert compressed != original_bytes
    
    decompressed = deflate_decompress(compressed)
    assert decompressed == original_bytes

def test_different_compression_levels():
    """Test different compression levels"""
    text = "Repeat " * 100  # Create a compressible text
    
    # Test various compression levels
    for level in range(10):
        compressed = deflate_compress(text, compression_level=level)
        decompressed = deflate_decompress(compressed)
        assert decompressed.decode('utf-8') == text

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        deflate_compress(123)
    
    with pytest.raises(TypeError):
        deflate_decompress(123)

def test_invalid_compression_level():
    """Test error handling for invalid compression levels"""
    with pytest.raises(ValueError):
        deflate_compress("test", compression_level=-1)
    
    with pytest.raises(ValueError):
        deflate_compress("test", compression_level=10)

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_text = ""
    compressed = deflate_compress(empty_text)
    decompressed = deflate_decompress(compressed)
    assert decompressed.decode('utf-8') == empty_text

def test_large_input():
    """Test compression of a large input"""
    large_text = "Large text " * 10000
    compressed = deflate_compress(large_text)
    assert len(compressed) < len(large_text.encode('utf-8'))
    
    decompressed = deflate_decompress(compressed)
    assert decompressed.decode('utf-8') == large_text