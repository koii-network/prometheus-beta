import pytest
from src.shannon_fano import shannon_fano_coding, shannon_fano_encode, shannon_fano_decode

def test_shannon_fano_coding_basic():
    """Test basic Shannon-Fano coding generation"""
    data = "AABBBCCCC"
    codes = shannon_fano_coding(data)
    
    # Verify codes are generated
    assert len(codes) == 3
    assert set(codes.keys()) == set('ABC')
    
    # Verify code uniqueness
    assert len(set(codes.values())) == 3

def test_shannon_fano_encode_decode():
    """Test encoding and decoding a simple string"""
    data = "HELLO WORLD"
    codes = shannon_fano_coding(data)
    
    # Encode the data
    encoded = shannon_fano_encode(data, codes)
    
    # Decode the data
    decoded = shannon_fano_decode(encoded, codes)
    
    assert decoded == data

def test_shannon_fano_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        shannon_fano_coding("")

def test_shannon_fano_single_char():
    """Test encoding and decoding with a single character"""
    data = "AAAAA"
    codes = shannon_fano_coding(data)
    
    assert len(codes) == 1
    assert codes['A'] == ''  # Single character gets empty code
    
    encoded = shannon_fano_encode(data, codes)
    decoded = shannon_fano_decode(encoded, codes)
    
    assert decoded == data

def test_shannon_fano_invalid_decode():
    """Test decoding with invalid encoded data"""
    data = "HELLO"
    codes = shannon_fano_coding(data)
    
    with pytest.raises(ValueError, match="Invalid encoded data"):
        shannon_fano_decode("1010101", codes)

def test_shannon_fano_frequency_distribution():
    """Test that more frequent characters get shorter codes"""
    data = "AAAAABBBBBCCCCCDDDDD"
    codes = shannon_fano_coding(data)
    
    # Validate code lengths based on frequency
    code_lengths = {char: len(code) for char, code in codes.items()}
    
    assert code_lengths['A'] <= code_lengths['B']
    assert code_lengths['B'] <= code_lengths['C']
    assert code_lengths['C'] <= code_lengths['D']