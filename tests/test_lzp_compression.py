import pytest
from src.lzp_compression import lzp_compress, lzp_decompress

def test_lzp_empty_input():
    """Test compression and decompression of empty input"""
    empty_data = b''
    compressed = lzp_compress(empty_data)
    assert compressed == b''
    
    decompressed = lzp_decompress(compressed)
    assert decompressed == b''

def test_lzp_simple_compression():
    """Test basic compression and decompression"""
    original_data = b'hello world hello world'
    compressed = lzp_compress(original_data)
    decompressed = lzp_decompress(compressed)
    
    assert decompressed == original_data

def test_lzp_repeated_pattern():
    """Test compression of data with repeated patterns"""
    repeated_data = b'ABCABCABCABC' * 10
    compressed = lzp_compress(repeated_data)
    decompressed = lzp_decompress(compressed)
    
    assert decompressed == repeated_data

def test_lzp_random_data():
    """Test compression of random data"""
    import os
    random_data = os.urandom(1000)
    compressed = lzp_compress(random_data)
    decompressed = lzp_decompress(compressed)
    
    assert decompressed == random_data

def test_lzp_invalid_input_type():
    """Test that non-bytes input raises TypeError"""
    with pytest.raises(TypeError):
        lzp_compress("not bytes")
    
    with pytest.raises(TypeError):
        lzp_decompress("not bytes")

def test_lzp_error_handling():
    """Test error scenarios during decompression"""
    # Incomplete compressed data
    with pytest.raises(ValueError):
        lzp_decompress(b'\x01')
    
    # Malformed compressed data
    with pytest.raises(ValueError):
        lzp_decompress(b'\x00\x00\x00')  # Multiple prediction flags without context