import pytest
from src.lzh_compression import LZHCompressor

def test_lzh_compression_basic():
    """Test basic compression and decompression"""
    original_data = b'hello world hello world'
    compressed = LZHCompressor.compress(original_data)
    decompressed = LZHCompressor.decompress(compressed)
    
    assert decompressed == original_data

def test_lzh_compression_empty_input():
    """Test compression and decompression of empty input"""
    original_data = b''
    compressed = LZHCompressor.compress(original_data)
    decompressed = LZHCompressor.decompress(compressed)
    
    assert decompressed == original_data

def test_lzh_compression_repeated_pattern():
    """Test compression of data with repeated patterns"""
    original_data = b'abcabcabcabcabcabc' * 10
    compressed = LZHCompressor.compress(original_data)
    decompressed = LZHCompressor.decompress(compressed)
    
    assert decompressed == original_data

def test_lzh_compression_type_error():
    """Test type error handling"""
    with pytest.raises(TypeError):
        LZHCompressor.compress("not bytes")
    
    with pytest.raises(TypeError):
        LZHCompressor.decompress("not bytes")

def test_lzh_compression_varied_data():
    """Test compression of varied data"""
    original_data = b'This is a test of the LZH compression algorithm with some random data!'
    compressed = LZHCompressor.compress(original_data)
    decompressed = LZHCompressor.decompress(compressed)
    
    assert decompressed == original_data