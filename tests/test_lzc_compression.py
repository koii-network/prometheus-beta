import pytest
from src.lzc_compression import lzc_compress

def test_lzc_compress_basic():
    """Test basic compression of a simple string."""
    input_data = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzc_compress(input_data)
    assert isinstance(compressed, list)
    assert all(isinstance(code, int) for code in compressed)
    assert len(compressed) > 0

def test_lzc_compress_empty_input():
    """Test compression of an empty input."""
    input_data = ""
    compressed = lzc_compress(input_data)
    assert compressed == []

def test_lzc_compress_single_char():
    """Test compression of a single character."""
    input_data = "A"
    compressed = lzc_compress(input_data)
    assert compressed == [ord('A')]

def test_lzc_compress_repeated_pattern():
    """Test compression of a repeated pattern."""
    input_data = "ABABABABAB"
    compressed = lzc_compress(input_data)
    assert isinstance(compressed, list)
    assert len(compressed) < len(input_data)

def test_lzc_compress_bytes_input():
    """Test compression with bytes input."""
    input_data = b'\x01\x02\x03\x01\x02\x03'
    compressed = lzc_compress(input_data)
    assert isinstance(compressed, list)
    assert all(isinstance(code, int) for code in compressed)

def test_lzc_compress_invalid_input():
    """Test that TypeError is raised for invalid input types."""
    with pytest.raises(TypeError):
        lzc_compress(123)
    
    with pytest.raises(TypeError):
        lzc_compress(None)
    
    with pytest.raises(TypeError):
        lzc_compress(['a', 'b', 'c'])