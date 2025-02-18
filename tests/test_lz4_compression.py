import pytest
from src.lz4_compression import lz4_compress, lz4_decompress

def test_lz4_compression_basic():
    """Test basic compression and decompression"""
    original = b'hello world hello world'
    compressed = lz4_compress(original)
    assert compressed != original
    decompressed = lz4_decompress(compressed)
    assert decompressed == original

def test_lz4_empty_input():
    """Test compression and decompression of empty input"""
    empty = b''
    compressed = lz4_compress(empty)
    assert compressed == b''
    decompressed = lz4_decompress(compressed)
    assert decompressed == b''

def test_lz4_repeated_pattern():
    """Test compression of repeated patterns"""
    repeated = b'ABCABCABCABC' * 10
    compressed = lz4_compress(repeated)
    assert compressed != repeated
    decompressed = lz4_decompress(compressed)
    assert decompressed == repeated

def test_lz4_random_data():
    """Test compression of random data"""
    import os
    random_data = os.urandom(1000)
    compressed = lz4_compress(random_data)
    decompressed = lz4_decompress(compressed)
    assert decompressed == random_data

def test_lz4_type_error():
    """Test that type errors are raised for invalid inputs"""
    with pytest.raises(TypeError):
        lz4_compress("not bytes")
    
    with pytest.raises(TypeError):
        lz4_decompress("not bytes")

def test_lz4_large_input():
    """Test compression of a large input"""
    large_input = b'test' * 10000
    compressed = lz4_compress(large_input)
    decompressed = lz4_decompress(compressed)
    assert decompressed == large_input