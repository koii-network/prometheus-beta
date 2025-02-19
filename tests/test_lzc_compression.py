import pytest
from src.lzc_compression import lzc_compress, lzc_decompress

def test_lzc_basic_compression():
    """Test basic compression and decompression of a simple string."""
    test_string = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzc_compress(test_string)
    
    # Basic checks
    assert len(compressed) > 0
    assert len(compressed) < len(test_string)
    
    # Verify round-trip compression
    decompressed = lzc_decompress(compressed)
    assert decompressed.decode('utf-8') == test_string

def test_lzc_empty_input():
    """Test compression and decompression of empty input."""
    test_string = ""
    compressed = lzc_compress(test_string)
    assert compressed == []
    
    decompressed = lzc_decompress(compressed)
    assert decompressed == b''

def test_lzc_single_character():
    """Test compression and decompression of a single character."""
    test_string = "A"
    compressed = lzc_compress(test_string)
    assert compressed == [65]  # ASCII code for 'A'
    
    decompressed = lzc_decompress(compressed)
    assert decompressed.decode('utf-8') == test_string

def test_lzc_bytes_input():
    """Test compression and decompression of bytes input."""
    test_bytes = b'\x00\x01\x02\x03'
    compressed = lzc_compress(test_bytes)
    
    # Basic checks
    assert len(compressed) > 0
    
    decompressed = lzc_decompress(compressed)
    assert decompressed == test_bytes

def test_lzc_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        lzc_compress(123)
    
    with pytest.raises(TypeError):
        lzc_decompress(123)
    
    with pytest.raises(TypeError):
        lzc_decompress([1, 2, 'a'])

def test_lzc_repeated_patterns():
    """Test compression of input with repeated patterns."""
    test_string = "ABABABABABABABABAB"
    compressed = lzc_compress(test_string)
    
    # Basic checks
    assert len(compressed) > 0
    assert len(compressed) < len(test_string)
    
    decompressed = lzc_decompress(compressed)
    assert decompressed.decode('utf-8') == test_string

def test_lzc_long_input():
    """Test compression of a longer input with varied patterns."""
    test_string = "Hello, hello, hello world! Hello, hello, hello world!"
    compressed = lzc_compress(test_string)
    
    # Basic checks
    assert len(compressed) > 0
    assert len(compressed) < len(test_string)
    
    decompressed = lzc_decompress(compressed)
    assert decompressed.decode('utf-8') == test_string