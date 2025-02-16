import pytest
from src.lzp_compression import lzp_compress, lzp_decompress

def test_lzp_compress_decompress_empty():
    """Test compression and decompression of empty bytes."""
    data = b''
    compressed = lzp_compress(data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == data

def test_lzp_compress_decompress_simple():
    """Test compression and decompression of a simple byte sequence."""
    data = b'hello world hello world'
    compressed = lzp_compress(data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == data

def test_lzp_compress_decompress_repeated_pattern():
    """Test compression with a highly repetitive pattern."""
    data = b'abcabcabcabcabcabc' * 10
    compressed = lzp_compress(data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == data

def test_lzp_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        lzp_compress("not bytes")
    
    with pytest.raises(TypeError):
        lzp_decompress("not bytes")

def test_lzp_random_data():
    """Test compression and decompression with random data."""
    import random
    data = bytes(random.randint(0, 255) for _ in range(1000))
    compressed = lzp_compress(data)
    decompressed = lzp_decompress(compressed)
    assert decompressed == data