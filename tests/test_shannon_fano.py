import pytest
from src.shannon_fano import shannon_fano_coding, shannon_fano_encode, shannon_fano_decode

def test_shannon_fano_basic():
    """Test basic Shannon-Fano coding functionality"""
    data = "AABBBCCCC"
    codes = shannon_fano_coding(data)
    
    # Verify codes are generated
    assert len(codes) > 0
    assert all(isinstance(code, str) for code in codes.values())
    
    # Verify encoding and decoding
    encoded = shannon_fano_encode(data, codes)
    decoded = shannon_fano_decode(encoded, codes)
    assert decoded == data

def test_shannon_fano_different_inputs():
    """Test Shannon-Fano coding with different input types"""
    # String input
    str_data = "hello world"
    str_codes = shannon_fano_coding(str_data)
    str_encoded = shannon_fano_encode(str_data, str_codes)
    str_decoded = shannon_fano_decode(str_encoded, str_codes)
    assert str_decoded == str_data
    
    # List input
    list_data = ['a', 'b', 'c', 'a', 'b', 'c']
    list_codes = shannon_fano_coding(list_data)
    list_encoded = shannon_fano_encode(list_data, list_codes)
    list_decoded = shannon_fano_decode(list_encoded, list_codes)
    assert list_decoded == ''.join(list_data)

def test_shannon_fano_edge_cases():
    """Test edge cases for Shannon-Fano coding"""
    # Single character input
    single_char_data = "A"
    single_char_codes = shannon_fano_coding(single_char_data)
    single_char_encoded = shannon_fano_encode(single_char_data, single_char_codes)
    single_char_decoded = shannon_fano_decode(single_char_encoded, single_char_codes)
    assert single_char_decoded == single_char_data
    
    # Empty input should raise ValueError
    with pytest.raises(ValueError):
        shannon_fano_coding("")
    
    # Decoding invalid data should raise ValueError
    codes = shannon_fano_coding("ABCD")
    with pytest.raises(ValueError):
        shannon_fano_decode("10101010101", codes)

def test_shannon_fano_unique_codes():
    """Verify that generated codes are unique"""
    data = "AABBBCCCCDDDD"
    codes = shannon_fano_coding(data)
    
    # Check that all codes are unique
    assert len(set(codes.values())) == len(codes)

def test_shannon_fano_prefix_free():
    """Verify that generated codes form a prefix-free code"""
    data = "AABBBCCCCDDDD"
    codes = shannon_fano_coding(data)
    
    # Simple check for prefix-free property
    for code1 in codes.values():
        for code2 in codes.values():
            if code1 != code2:
                assert not (code1.startswith(code2) or code2.startswith(code1))