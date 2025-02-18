import pytest
from src.lzp_compression import lzp_compress, lzp_decompress

def test_lzp_compression_empty_input():
    """Test compression and decompression of empty input"""
    data = b''
    compressed = lzp_compress(data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == data

def test_lzp_compression_simple_sequence():
    """Test compression and decompression of a simple byte sequence"""
    data = b'hello world'
    compressed = lzp_compress(data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == data

def test_lzp_compression_repeated_pattern():
    """Test compression of data with repeated patterns"""
    data = b'aaaabbbbccccdddd'
    compressed = lzp_compress(data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == data

def test_lzp_compression_large_input():
    """Test compression of a larger input"""
    data = b''.join([bytes([i % 256]) for i in range(1000)])
    compressed = lzp_compress(data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == data

def test_lzp_compression_input_type_error():
    """Test that TypeError is raised for non-bytes input"""
    with pytest.raises(TypeError):
        lzp_compress("not bytes")
    
    with pytest.raises(TypeError):
        lzp_decompress("not bytes")