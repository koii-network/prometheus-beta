import pytest
import sys
sys.path.append('src')

from lzma2_compression import compress_lzma2, decompress_lzma2

def test_compress_decompress_string():
    """Test compression and decompression of a string"""
    original = "Hello, world! This is a test of LZMA2 compression."
    compressed = compress_lzma2(original)
    assert compressed  # Ensure compression produces output
    assert len(compressed) < len(original.encode('utf-8'))  # Compression reduces size
    
    decompressed = decompress_lzma2(compressed)
    assert decompressed.decode('utf-8') == original

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes"""
    original = b'\x00\x01\x02\x03\x04' * 100
    compressed = compress_lzma2(original)
    assert compressed  # Ensure compression produces output
    assert len(compressed) < len(original)  # Compression reduces size
    
    decompressed = decompress_lzma2(compressed)
    assert decompressed == original

def test_compression_levels():
    """Test different compression levels"""
    text = "This is a test of various compression levels in LZMA2"
    
    # Test all compression levels
    for level in range(10):
        compressed = compress_lzma2(text, compression_level=level)
        decompressed = decompress_lzma2(compressed)
        assert decompressed.decode('utf-8') == text

def test_invalid_compression_level():
    """Test handling of invalid compression levels"""
    with pytest.raises(ValueError):
        compress_lzma2("test", compression_level=-1)
    
    with pytest.raises(ValueError):
        compress_lzma2("test", compression_level=10)

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        compress_lzma2(123)
    
    with pytest.raises(TypeError):
        decompress_lzma2("not bytes")

def test_empty_input():
    """Test handling of empty inputs"""
    empty_string = ""
    empty_bytes = b""
    
    # Compression of empty input should work
    compressed_str = compress_lzma2(empty_string)
    compressed_bytes = compress_lzma2(empty_bytes)
    
    # Decompression of empty input should work
    assert decompress_lzma2(compressed_str) == b""
    assert decompress_lzma2(compressed_bytes) == b""

def test_invalid_compressed_data():
    """Test handling of invalid compressed data"""
    with pytest.raises(RuntimeError):
        decompress_lzma2(b'invalid compressed data')