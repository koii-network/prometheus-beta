import pytest
import zlib
from src.deflate_compression import deflate_compress, deflate_decompress

def test_deflate_compress_text():
    """Test compression of text data"""
    input_text = "Hello, world! This is a test of Deflate compression."
    compressed = deflate_compress(input_text)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(input_text.encode('utf-8'))

def test_deflate_compress_bytes():
    """Test compression of bytes data"""
    input_bytes = b"Binary data compression test"
    compressed = deflate_compress(input_bytes)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(input_bytes)

def test_deflate_compression_levels():
    """Test different compression levels"""
    input_data = "Test compression levels" * 100
    for level in range(10):
        compressed = deflate_compress(input_data, level)
        assert isinstance(compressed, bytes)

def test_deflate_decompress():
    """Test decompression of compressed data"""
    input_text = "Hello, world! This is a test of Deflate compression."
    compressed = deflate_compress(input_text)
    decompressed = deflate_decompress(compressed)
    assert decompressed.decode('utf-8') == input_text

def test_roundtrip_compression():
    """Test full compression and decompression cycle"""
    input_data = "Test full roundtrip compression and decompression"
    compressed = deflate_compress(input_data)
    decompressed = deflate_decompress(compressed)
    assert decompressed.decode('utf-8') == input_data

def test_invalid_compression_level():
    """Test handling of invalid compression levels"""
    input_text = "Test invalid compression level"
    with pytest.raises(ValueError):
        deflate_compress(input_text, -1)
    with pytest.raises(ValueError):
        deflate_compress(input_text, 10)

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        deflate_compress(123)
    with pytest.raises(TypeError):
        deflate_decompress("not bytes")

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_text = ""
    compressed = deflate_compress(empty_text)
    decompressed = deflate_decompress(compressed)
    assert decompressed == b""