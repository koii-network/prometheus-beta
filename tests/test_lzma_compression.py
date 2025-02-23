"""
Unit tests for LZMA compression module.

This test suite covers various scenarios for compression and decompression,
including edge cases, error handling, and basic functionality.
"""

import pytest
import lzma
from src.lzma_compression import compress_lzma, decompress_lzma

def test_compress_decompress_string():
    """Test compression and decompression of a string."""
    original_text = "Hello, world! This is a test of LZMA compression."
    compressed = compress_lzma(original_text)
    assert compressed != original_text.encode('utf-8')
    
    decompressed = decompress_lzma(compressed)
    assert decompressed.decode('utf-8') == original_text

def test_compress_decompress_bytes():
    """Test compression and decompression of bytes."""
    original_bytes = b'\x00\x01\x02\x03\x04\x05'
    compressed = compress_lzma(original_bytes)
    assert compressed != original_bytes
    
    decompressed = decompress_lzma(compressed)
    assert decompressed == original_bytes

def test_compress_preset_levels():
    """Test different compression presets."""
    data = "Compression level test" * 100
    
    # Test various preset levels
    for preset in range(10):
        compressed = compress_lzma(data, preset=preset)
        decompressed = decompress_lzma(compressed)
        assert decompressed.decode('utf-8') == data

def test_compress_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        compress_lzma(123)
    
    with pytest.raises(TypeError):
        compress_lzma(None)
    
    with pytest.raises(TypeError):
        compress_lzma([1, 2, 3])

def test_compress_invalid_preset():
    """Test error handling for invalid compression preset."""
    with pytest.raises(ValueError):
        compress_lzma("Test", preset=-1)
    
    with pytest.raises(ValueError):
        compress_lzma("Test", preset=10)

def test_decompress_invalid_input():
    """Test error handling for invalid input to decompression."""
    with pytest.raises(TypeError):
        decompress_lzma("Not bytes")
    
    with pytest.raises(TypeError):
        decompress_lzma(123)

def test_decompress_invalid_compressed_data():
    """Test decompression of invalid compressed data."""
    with pytest.raises(lzma.LZMAError):
        decompress_lzma(b'Invalid compressed data')

def test_large_data_compression():
    """Test compression and decompression of large data."""
    large_data = "This is a large text " * 10000
    compressed = compress_lzma(large_data)
    decompressed = decompress_lzma(compressed)
    assert decompressed.decode('utf-8') == large_data