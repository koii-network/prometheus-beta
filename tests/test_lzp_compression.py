import pytest
from src.lzp_compression import lzp_compress, lzp_decompress

def test_lzp_compression_basic():
    """Test basic compression and decompression"""
    original = b'hello world hello world'
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_empty_input():
    """Test compression and decompression of empty input"""
    assert lzp_compress(b'') == b''
    assert lzp_decompress(b'') == b''

def test_lzp_repeated_bytes():
    """Test compression of repeated bytes"""
    original = b'\x00\x00\x00\x00\x01\x01\x01\x01'
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_random_bytes():
    """Test compression of random bytes"""
    import os
    original = os.urandom(1000)
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        lzp_compress("not bytes")
    with pytest.raises(TypeError):
        lzp_decompress("not bytes")

def test_lzp_corrupt_compressed_data():
    """Test handling of corrupt compressed data"""
    with pytest.raises(ValueError):
        lzp_decompress(b'\xFF')  # Incomplete compressed data