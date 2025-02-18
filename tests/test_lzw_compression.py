import pytest
from src.lzw_compression import lzw_compress

def test_lzw_compress_basic():
    """Test basic compression of a simple string."""
    input_str = "ABRACADABRA"
    compressed = lzw_compress(input_str)
    assert isinstance(compressed, list)
    assert all(isinstance(x, int) for x in compressed)
    assert len(compressed) > 0

def test_lzw_compress_single_char():
    """Test compression of a single character string."""
    input_str = "A"
    compressed = lzw_compress(input_str)
    assert compressed == [ord('A')]

def test_lzw_compress_repeated_pattern():
    """Test compression of a string with repeated patterns."""
    input_str = "AAAAAAAA"
    compressed = lzw_compress(input_str)
    assert len(compressed) < len(input_str)

def test_lzw_compress_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        lzw_compress(123)
    
    with pytest.raises(TypeError):
        lzw_compress(None)
    
    with pytest.raises(TypeError):
        lzw_compress(["test"])

def test_lzw_compress_empty_string():
    """Test error handling for empty string."""
    with pytest.raises(ValueError):
        lzw_compress("")