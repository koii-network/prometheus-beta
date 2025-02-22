import pytest
import sys
sys.path.append('src')

from lzc_compression import lzc_compress

def test_lzc_compress_basic():
    """Test basic compression with simple input"""
    input_data = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzc_compress(input_data)
    
    # Verify compression generates codes
    assert len(compressed) > 0
    assert all(isinstance(code, int) for code in compressed)

def test_lzc_compress_single_char():
    """Test compression of a single character"""
    input_data = "A"
    compressed = lzc_compress(input_data)
    
    # Single char should result in its ASCII code
    assert len(compressed) == 1
    assert compressed[0] == ord('A')

def test_lzc_compress_empty_input():
    """Test that empty input raises a ValueError"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzc_compress("")

def test_lzc_compress_invalid_input():
    """Test that invalid input types raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be a string or bytes"):
        lzc_compress(12345)
    with pytest.raises(TypeError, match="Input must be a string or bytes"):
        lzc_compress(None)

def test_lzc_compress_bytes_input():
    """Test compression with bytes input"""
    input_data = b'\x01\x02\x03\x01\x02\x03'
    compressed = lzc_compress(input_data)
    
    # Verify compression generates codes
    assert len(compressed) > 0
    assert all(isinstance(code, int) for code in compressed)

def test_lzc_compress_repeated_patterns():
    """Test compression of data with repeated patterns"""
    input_data = "ABABABABABABABAB"
    compressed = lzc_compress(input_data)
    
    # Verify compression generates codes and reduces length
    assert len(compressed) < len(input_data)
    assert all(isinstance(code, int) for code in compressed)