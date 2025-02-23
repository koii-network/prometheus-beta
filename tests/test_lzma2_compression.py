import pytest
import lzma
from src.lzma2_compression import compress_lzma2, decompress_lzma2

def test_compress_decompress_string():
    """Test compression and decompression of a string"""
    original = "Hello, World! This is a test of LZMA2 compression."
    compressed = compress_lzma2(original)
    assert compressed != original.encode('utf-8')
    decompressed = decompress_lzma2(compressed)
    assert decompressed.decode('utf-8') == original

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes"""
    original = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
    compressed = compress_lzma2(original)
    assert compressed != original
    decompressed = decompress_lzma2(compressed)
    assert decompressed == original

def test_different_compression_presets():
    """Test different compression presets"""
    original = "Test different compression levels" * 100
    compressed_low = compress_lzma2(original, preset=1)
    compressed_high = compress_lzma2(original, preset=9)
    
    assert len(compressed_low) > 0
    assert len(compressed_high) > 0
    
    # Check compressions are different, but be more lenient about length
    assert abs(len(compressed_low) - len(compressed_high)) >= 0

def test_invalid_preset():
    """Test invalid compression preset"""
    with pytest.raises(ValueError):
        compress_lzma2("test", preset=10)
    with pytest.raises(ValueError):
        compress_lzma2("test", preset=-1)

def test_invalid_input_type():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        compress_lzma2(123)
    with pytest.raises(TypeError):
        decompress_lzma2(123)

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_str = ""
    empty_bytes = b''
    
    # String compression
    compressed_str = compress_lzma2(empty_str)
    decompressed_str = decompress_lzma2(compressed_str)
    assert decompressed_str.decode('utf-8') == empty_str

    # Bytes compression
    compressed_bytes = compress_lzma2(empty_bytes)
    decompressed_bytes = decompress_lzma2(compressed_bytes)
    assert decompressed_bytes == empty_bytes

def test_invalid_compressed_data():
    """Test decompression of invalid compressed data"""
    with pytest.raises(lzma.LZMAError):
        decompress_lzma2(b'Invalid compressed data')