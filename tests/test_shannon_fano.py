import pytest
from src.shannon_fano import shannon_fano_coding, encode_data, decode_data

def test_shannon_fano_basic():
    """Test basic Shannon-Fano coding functionality"""
    data = "AABBBCCCC"
    codes = shannon_fano_coding(data)
    
    # Verify codes are generated for all unique symbols
    assert set(codes.keys()) == set("ABC")
    assert len(codes) == 3
    
    # Verify encoding and decoding
    encoded = encode_data(data, codes)
    decoded = decode_data(encoded, codes)
    assert decoded == data

def test_shannon_fano_string_input():
    """Test Shannon-Fano coding with string input"""
    data = "hello world"
    codes = shannon_fano_coding(data)
    
    # Verify codes are generated for all unique symbols
    assert set(codes.keys()) == set(" helowrd")
    
    # Verify encoding and decoding
    encoded = encode_data(data, codes)
    decoded = decode_data(encoded, codes)
    assert decoded == data

def test_shannon_fano_complex_input():
    """Test Shannon-Fano coding with more complex input"""
    data = "abracadabra"
    codes = shannon_fano_coding(data)
    
    # Verify codes are generated for all unique symbols
    assert set(codes.keys()) == set("abcdr")
    
    # Verify encoding and decoding
    encoded = encode_data(data, codes)
    decoded = decode_data(encoded, codes)
    assert decoded == data

def test_shannon_fano_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError):
        shannon_fano_coding([])
    
    with pytest.raises(ValueError):
        shannon_fano_coding("")

def test_shannon_fano_encode_unknown_symbol():
    """Test encoding with unknown symbol"""
    data = "hello"
    codes = shannon_fano_coding(data)
    
    with pytest.raises(ValueError):
        encode_data("hello world", codes)

def test_shannon_fano_decode_invalid():
    """Test decoding with invalid encoded data"""
    data = "hello"
    codes = shannon_fano_coding(data)
    
    with pytest.raises(ValueError):
        decode_data("10101010101", codes)

def test_shannon_fano_single_symbol():
    """Test Shannon-Fano coding with single symbol"""
    data = "aaaaa"
    codes = shannon_fano_coding(data)
    
    assert codes == {'a': '0'}
    
    encoded = encode_data(data, codes)
    decoded = decode_data(encoded, codes)
    assert decoded == data