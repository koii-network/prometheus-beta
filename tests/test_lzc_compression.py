import pytest
from src.lzc_compression import lzc_compress

def test_lzc_compress_basic():
    """Test basic compression of a simple string."""
    result = lzc_compress("TOBEORNOTTOBEORTOBEORNOT")
    assert isinstance(result, list)
    assert len(result) > 0

def test_lzc_compress_single_char():
    """Test compression of a single character."""
    result = lzc_compress("A")
    assert result == [ord('A')]

def test_lzc_compress_repeated_pattern():
    """Test compression of a string with repeated patterns."""
    result = lzc_compress("ABABABABAB")
    assert len(result) < len("ABABABABAB")

def test_lzc_compress_empty_string():
    """Test that empty string raises ValueError."""
    with pytest.raises(ValueError):
        lzc_compress("")

def test_lzc_compress_non_string_input():
    """Test that non-string input raises TypeError."""
    with pytest.raises(TypeError):
        lzc_compress(12345)
    with pytest.raises(TypeError):
        lzc_compress(None)

def test_lzc_compress_unicode():
    """Test compression with Unicode characters."""
    result = lzc_compress("Hello, 世界!")
    assert isinstance(result, list)
    assert len(result) > 0

def test_lzc_compress_long_string():
    """Test compression of a longer string."""
    long_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 10
    result = lzc_compress(long_string)
    assert len(result) < len(long_string)