import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data

def test_compress_decompress_text():
    """Test compression and decompression of text data"""
    original_text = "Hello, world! This is a test of Zlib compression."
    compressed = compress_data(original_text)
    decompressed = decompress_data(compressed)
    assert decompressed.decode('utf-8') == original_text

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes data"""
    original_bytes = b'\x00\x01\x02\x03\x04'
    compressed = compress_data(original_bytes)
    decompressed = decompress_data(compressed)
    assert decompressed == original_bytes

def test_compression_levels():
    """Test different compression levels"""
    data = "Test compression levels" * 100
    levels = [0, 3, 6, 9]
    compressed_sizes = [len(compress_data(data, level)) for level in levels]
    
    # Generally, higher compression levels result in smaller compressed sizes
    for i in range(len(levels) - 1):
        assert compressed_sizes[i] >= compressed_sizes[i+1]

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data("not bytes")

def test_invalid_compression_level():
    """Test handling of invalid compression levels"""
    with pytest.raises(ValueError):
        compress_data("test", compression_level=10)
    
    with pytest.raises(ValueError):
        compress_data("test", compression_level=-1)

def test_decompress_invalid_data():
    """Test decompression of invalid compressed data"""
    with pytest.raises(zlib.error):
        decompress_data(b'invalid compressed data')

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_text = ""
    empty_bytes = b''
    
    compressed_text = compress_data(empty_text)
    decompressed_text = decompress_data(compressed_text)
    assert decompressed_text.decode('utf-8') == empty_text
    
    compressed_bytes = compress_data(empty_bytes)
    decompressed_bytes = decompress_data(compressed_bytes)
    assert decompressed_bytes == empty_bytes