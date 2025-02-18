import pytest
import lzma
from src.lzma2_compression import compress_lzma2, decompress_lzma2

def test_compress_lzma2_bytes():
    """Test compression of byte data"""
    test_data = b'Hello, this is a test string for LZMA2 compression!'
    compressed = compress_lzma2(test_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(test_data)

def test_compress_lzma2_str():
    """Test compression of string data"""
    test_data = 'Hello, this is a test string for LZMA2 compression!'
    compressed = compress_lzma2(test_data)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(test_data.encode('utf-8'))

def test_lzma2_compression_decompression():
    """Test full compression and decompression cycle"""
    test_data = b'Hello, this is a test string for LZMA2 compression!'
    compressed = compress_lzma2(test_data)
    decompressed = decompress_lzma2(compressed)
    assert decompressed == test_data

def test_compress_lzma2_different_presets():
    """Test compression with different preset levels"""
    test_data = b'Hello, this is a test string for LZMA2 compression!'
    compressed_low = compress_lzma2(test_data, preset=1)
    compressed_mid = compress_lzma2(test_data, preset=5)
    compressed_high = compress_lzma2(test_data, preset=9)
    
    assert len(compressed_low) >= len(compressed_mid)
    assert len(compressed_mid) >= len(compressed_high)

def test_compress_lzma2_invalid_input_type():
    """Test compression with invalid input type"""
    with pytest.raises(TypeError):
        compress_lzma2(123)
    
    with pytest.raises(TypeError):
        compress_lzma2(None)

def test_compress_lzma2_invalid_preset():
    """Test compression with invalid preset"""
    with pytest.raises(ValueError):
        compress_lzma2(b'test', preset=-1)
    
    with pytest.raises(ValueError):
        compress_lzma2(b'test', preset=10)

def test_decompress_lzma2_invalid_input():
    """Test decompression with invalid input"""
    with pytest.raises(TypeError):
        decompress_lzma2('not bytes')
    
    with pytest.raises(TypeError):
        decompress_lzma2(None)
    
    with pytest.raises(lzma.LZMAError):
        decompress_lzma2(b'invalid compressed data')

def test_large_data_compression():
    """Test compression of large data"""
    test_data = b'A' * 100000  # 100 KB of repeated data
    compressed = compress_lzma2(test_data)
    assert len(compressed) < len(test_data)
    
    decompressed = decompress_lzma2(compressed)
    assert decompressed == test_data