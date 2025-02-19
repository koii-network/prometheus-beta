import pytest
from src.lzc_compression import lzc_compress

def test_lzc_compress_basic():
    """Test basic compression of simple string"""
    input_data = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzc_compress(input_data)
    assert isinstance(compressed, list)
    assert all(isinstance(code, int) for code in compressed)
    assert len(compressed) < len(input_data)

def test_lzc_compress_bytes():
    """Test compression with bytes input"""
    input_data = b"Hello, hello, hello world!"
    compressed = lzc_compress(input_data)
    assert isinstance(compressed, list)
    assert all(isinstance(code, int) for code in compressed)

def test_lzc_compress_empty_input():
    """Test that empty input raises a ValueError"""
    with pytest.raises(ValueError):
        lzc_compress("")
    with pytest.raises(ValueError):
        lzc_compress(b"")

def test_lzc_compress_invalid_input():
    """Test that invalid input types raise a TypeError"""
    with pytest.raises(TypeError):
        lzc_compress(123)
    with pytest.raises(TypeError):
        lzc_compress(["not", "valid"])

def test_lzc_compress_repetitive_data():
    """Test compression of highly repetitive data"""
    input_data = "AAAAAAAAAAAAAAAAAAAA"
    compressed = lzc_compress(input_data)
    assert len(compressed) < len(input_data)

def test_lzc_compress_unique_data():
    """Test compression of unique data"""
    input_data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    compressed = lzc_compress(input_data)
    # Unique data might not compress much
    assert len(compressed) <= len(input_data)