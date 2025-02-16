import pytest
from src.shannon_fano import shannon_fano_coding, encode_text, decode_text

def test_shannon_fano_basic():
    """Test basic Shannon-Fano coding functionality"""
    text = "AAAAABBBCCCDDE"
    codes = shannon_fano_coding(text)
    
    # Verify codes are generated
    assert len(codes) > 0
    assert all(isinstance(code, str) for code in codes.values())
    
    # Encode and decode
    encoded = encode_text(text, codes)
    decoded = decode_text(encoded, codes)
    assert decoded == text

def test_shannon_fano_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError, match="Input text cannot be empty"):
        shannon_fano_coding("")

def test_shannon_fano_single_char():
    """Test input with single character"""
    text = "AAAAA"
    codes = shannon_fano_coding(text)
    assert codes == {'A': '0'}
    assert encode_text(text, codes) == '0' * len(text)
    assert decode_text('0' * len(text), codes) == text

def test_shannon_fano_unique_codes():
    """Test that generated codes are unique"""
    text = "AAAAABBBCCCDDE"
    codes = shannon_fano_coding(text)
    
    # Verify unique codes
    code_set = set(codes.values())
    assert len(code_set) == len(codes)

def test_shannon_fano_encode_decode():
    """Comprehensive encode-decode test"""
    test_cases = [
        "HELLO WORLD",
        "abcdefghijklmnopqrstuvwxyz",
        "1234567890",
        "MixEd CaSe TeXt 123!@#"
    ]
    
    for text in test_cases:
        codes = shannon_fano_coding(text)
        encoded = encode_text(text, codes)
        decoded = decode_text(encoded, codes)
        assert decoded == text

def test_shannon_fano_invalid_encode():
    """Test encoding with missing character"""
    codes = shannon_fano_coding("HELLO")
    with pytest.raises(ValueError, match="Character"):
        encode_text("WORLD", codes)

def test_shannon_fano_invalid_decode():
    """Test decoding with invalid encoded text"""
    codes = shannon_fano_coding("HELLO")
    with pytest.raises(ValueError, match="Unable to fully decode"):
        decode_text("10101010101", codes)