import pytest
from src.lzp_compression import lzp_compress, lzp_decompress

def test_lzp_compression_empty_input():
    """Test compression and decompression of empty input"""
    empty_input = b''
    compressed = lzp_compress(empty_input)
    decompressed = lzp_decompress(compressed)
    assert decompressed == empty_input

def test_lzp_compression_simple_data():
    """Test compression and decompression of simple data"""
    test_data = b'hello world hello world'
    compressed = lzp_compress(test_data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == test_data

def test_lzp_compression_repeated_pattern():
    """Test compression of data with repeated patterns"""
    test_data = b'abcabcabcabc' * 10
    compressed = lzp_compress(test_data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == test_data

def test_lzp_compression_random_data():
    """Test compression of random data"""
    import os
    test_data = os.urandom(1000)
    compressed = lzp_compress(test_data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == test_data

def test_lzp_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        lzp_compress("not bytes")
    with pytest.raises(TypeError):
        lzp_decompress("not bytes")

def test_invalid_compressed_data():
    """Test handling of invalid compressed data"""
    with pytest.raises(ValueError):
        lzp_decompress(b'\x02')  # Invalid flag
    with pytest.raises(ValueError):
        lzp_decompress(b'\x00')  # Incomplete literal