import pytest
import zlib
from src.deflate_compression import deflate_compress, deflate_decompress

def test_compress_decompress_text():
    """Test compression and decompression of text data"""
    original_text = "Hello, this is a test of Deflate compression!"
    compressed = deflate_compress(original_text)
    decompressed = deflate_decompress(compressed)
    assert decompressed.decode('utf-8') == original_text

def test_compress_decompress_bytes():
    """Test compression and decompression of byte data"""
    original_bytes = b'\x00\x01\x02\x03\x04\x05'
    compressed = deflate_compress(original_bytes)
    decompressed = deflate_decompress(compressed)
    assert decompressed == original_bytes

def test_compression_levels():
    """Test different compression levels"""
    text = "This is a test of compression levels" * 100
    
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
    empty_bytes = b''
    
    compressed_text = deflate_compress(empty_text)
    compressed_bytes = deflate_compress(empty_bytes)
    
    assert deflate_decompress(compressed_text) == b''
    assert deflate_decompress(compressed_bytes) == b''

def test_decompression_error():
    """Test decompression of invalid compressed data"""
    with pytest.raises(zlib.error):
        deflate_decompress(b'invalid compressed data')