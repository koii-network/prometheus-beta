import pytest
from src.lzw_compression import lzw_compress, lzw_decompress

def test_lzw_compression_basic():
    """Test basic compression and decompression"""
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_compression_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError):
        lzw_compress("")
    with pytest.raises(ValueError):
        lzw_decompress([])

def test_lzw_compression_invalid_input():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        lzw_compress(123)
    with pytest.raises(TypeError):
        lzw_decompress("not a list")

def test_lzw_compression_single_character():
    """Test compression of a single character"""
    original = "A"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_compression_repeated_pattern():
    """Test compression of a string with repeated patterns"""
    original = "ABABABABABABABAB"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_lzw_compression_long_string():
    """Test compression of a longer string"""
    original = "This is a longer test string with some repeated words words to test compression"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original