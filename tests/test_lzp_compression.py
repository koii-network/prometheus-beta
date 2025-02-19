import pytest
from src.lzp_compression import lzp_compress, lzp_decompress

def test_lzp_compression_basic():
    """Test basic compression and decompression"""
    original = b"Hello, world! This is a test of LZP compression."
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_compression_empty_input():
    """Test compression and decompression of empty input"""
    original = b""
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_compression_repeated_pattern():
    """Test compression of repeated patterns"""
    original = b"abcabcabcabcabcabc"
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original

def test_lzp_different_context_sizes():
    """Test compression with different context sizes"""
    original = b"Hello, world! This is a test of LZP compression."
    for context_size in [4, 8, 16]:
        compressed = lzp_compress(original, context_size)
        decompressed = lzp_decompress(compressed, context_size)
        assert decompressed == original

def test_lzp_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        lzp_compress("Not bytes")
    with pytest.raises(TypeError):
        lzp_decompress("Not bytes")

def test_lzp_invalid_context_size():
    """Test handling of invalid context sizes"""
    with pytest.raises(ValueError):
        lzp_compress(b"test", 0)
    with pytest.raises(ValueError):
        lzp_decompress(b"test", 0)

def test_lzp_random_data():
    """Test compression of random data"""
    import random
    random.seed(42)
    original = bytes(random.getrandbits(8) for _ in range(1000))
    compressed = lzp_compress(original)
    decompressed = lzp_decompress(compressed)
    assert decompressed == original