import pytest
from src.shannon_fano import shannon_fano_coding, shannon_fano_encode, shannon_fano_decode

def test_shannon_fano_basic():
    """Test basic Shannon-Fano coding functionality"""
    data = "AABBBCCCC"
    codes = shannon_fano_coding(data)
    
    # Verify codes are generated
    assert len(codes) > 0
    
    # Verify unique codes
    assert len(set(codes.values())) == len(codes)
    
    # Encode and decode
    encoded = shannon_fano_encode(data, codes)
    decoded = shannon_fano_decode(encoded, codes)
    
    assert decoded == data

def test_shannon_fano_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        shannon_fano_coding("")

def test_shannon_fano_single_char():
    """Test input with single character"""
    data = "AAAAA"
    codes = shannon_fano_coding(data)
    
    assert len(codes) == 1
    assert list(codes.keys())[0] == 'A'
    assert list(codes.values())[0] == '0'

def test_shannon_fano_multiple_chars():
    """Test input with multiple characters"""
    data = "hello world"
    codes = shannon_fano_coding(data)
    
    # Verify full encode-decode cycle
    encoded = shannon_fano_encode(data, codes)
    decoded = shannon_fano_decode(encoded, codes)
    
    assert decoded == data

def test_shannon_fano_decode_error():
    """Test decoding with invalid encoded string"""
    data = "hello"
    codes = shannon_fano_coding(data)
    
    # Try decoding with invalid binary string
    with pytest.raises(ValueError, match="Invalid encoded string"):
        shannon_fano_decode("11111", codes)

def test_shannon_fano_code_uniqueness():
    """Verify that generated codes are unique"""
    data = "AABBCCDDEE"
    codes = shannon_fano_coding(data)
    
    code_values = list(codes.values())
    assert len(code_values) == len(set(code_values)), "Codes must be unique"