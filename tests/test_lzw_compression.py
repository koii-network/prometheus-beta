import pytest
from src.lzw_compression import lzw_compress, lzw_decompress

def test_lzw_compress_basic():
    """Test basic compression of a simple string."""
    input_str = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzw_compress(input_str)
    assert isinstance(compressed, list)
    assert len(compressed) > 0

def test_lzw_decompress_basic():
    """Test basic decompression of a compressed string."""
    input_str = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzw_compress(input_str)
    decompressed = lzw_decompress(compressed)
    assert decompressed == input_str

def test_empty_string():
    """Test compression and decompression of an empty string."""
    input_str = ""
    compressed = lzw_compress(input_str)
    assert compressed == []
    
    decompressed = lzw_decompress(compressed)
    assert decompressed == ""

def test_single_character():
    """Test compression and decompression of a single character."""
    input_str = "A"
    compressed = lzw_compress(input_str)
    decompressed = lzw_decompress(compressed)
    assert decompressed == input_str

def test_repeated_string():
    """Test compression of a string with repeating patterns."""
    input_str = "ABABABABAB"
    compressed = lzw_compress(input_str)
    decompressed = lzw_decompress(compressed)
    assert decompressed == input_str

def test_input_type_errors():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        lzw_compress(123)
    
    with pytest.raises(TypeError):
        lzw_decompress(123)

def test_invalid_compressed_data():
    """Test error handling for invalid compressed data."""
    with pytest.raises(ValueError):
        lzw_decompress([1000000])  # An extremely large, invalid code