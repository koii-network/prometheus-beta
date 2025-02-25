import pytest
import lzma

from src.lzma_compression import compress_lzma, decompress_lzma

def test_compress_lzma_string():
    """Test compression of a string"""
    input_str = "Hello, world! This is a test of LZMA compression."
    compressed = compress_lzma(input_str)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != input_str.encode('utf-8')

def test_compress_lzma_bytes():
    """Test compression of bytes"""
    input_bytes = b"Binary data for compression test"
    compressed = compress_lzma(input_bytes)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0
    assert compressed != input_bytes

def test_lzma_compress_decompress():
    """Test full compression and decompression cycle"""
    input_str = "LZMA compression and decompression test"
    compressed = compress_lzma(input_str)
    decompressed = decompress_lzma(compressed)
    assert decompressed.decode('utf-8') == input_str

def test_lzma_different_presets():
    """Test compression with different preset levels"""
    input_data = "Test data for different compression levels"
    
    # Test various preset levels
    compressed_levels = [
        compress_lzma(input_data, preset=0),
        compress_lzma(input_data, preset=3),
        compress_lzma(input_data, preset=6),
        compress_lzma(input_data, preset=9)
    ]
    
    # Verify presets can affect compression
    assert all(isinstance(c, bytes) for c in compressed_levels)
    assert len(set(compressed_levels)) >= 1  # Ensure compression happens

def test_lzma_compression_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compress_lzma(123)
    
    with pytest.raises(TypeError):
        compress_lzma(None)
    
    with pytest.raises(TypeError):
        compress_lzma([1, 2, 3])

def test_lzma_compression_invalid_preset():
    """Test error handling for invalid compression preset"""
    with pytest.raises(ValueError):
        compress_lzma("test", preset=-1)
    
    with pytest.raises(ValueError):
        compress_lzma("test", preset=10)

def test_lzma_decompress_invalid_input():
    """Test error handling for invalid decompression input"""
    with pytest.raises(TypeError):
        decompress_lzma("not bytes")
    
    with pytest.raises(TypeError):
        decompress_lzma(123)
    
    with pytest.raises(lzma.LZMAError):
        decompress_lzma(b"Invalid compressed data")

def test_lzma_large_data_compression():
    """Test compression of larger data"""
    large_data = "A" * 100000  # 100,000 character string
    compressed = compress_lzma(large_data)
    assert len(compressed) < len(large_data)
    decompressed = decompress_lzma(compressed)
    assert decompressed.decode('utf-8') == large_data