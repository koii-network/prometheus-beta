import pytest
from src.shannon_fano import shannon_fano_encode, shannon_fano_decode

def test_shannon_fano_basic_encoding():
    """Test basic Shannon-Fano encoding"""
    data = "AABBBCCCC"
    codes = shannon_fano_encode(data)
    
    # Check that codes exist for each unique character
    assert set(codes.keys()) == set('ABC')
    assert len(set(codes.values())) == 3  # Unique codes
    
    # Verify frequency influences code length
    assert len(codes['C']) < len(codes['B'])
    assert len(codes['B']) < len(codes['A'])

def test_shannon_fano_encoding_decoding():
    """Test full encoding and decoding cycle"""
    data = "HELLO WORLD"
    codes = shannon_fano_encode(data)
    
    # Encode the data using the generated codes
    encoded_data = ''.join(codes[char] for char in data)
    
    # Decode back to original
    decoded = shannon_fano_decode(codes, encoded_data)
    assert decoded == data

def test_shannon_fano_empty_string():
    """Test encoding and decoding with empty string"""
    data = ""
    codes = shannon_fano_encode(data)
    assert codes == {}
    
    # Decoding empty string should also return empty string
    encoded = ""
    decoded = shannon_fano_decode(codes, encoded) if codes else ""
    assert decoded == ""

def test_shannon_fano_single_character():
    """Test encoding and decoding with single character repeats"""
    data = "AAAAA"
    codes = shannon_fano_encode(data)
    
    # Should have a single code of '0'
    assert codes == {'A': '0'}
    
    # Encode and decode
    encoded = ''.join(codes[char] for char in data)
    decoded = shannon_fano_decode(codes, encoded)
    assert decoded == data

def test_shannon_fano_invalid_decoding():
    """Test decoding with invalid encoded data"""
    data = "HELLO"
    codes = shannon_fano_encode(data)
    
    # Try decoding with an invalid code
    with pytest.raises(ValueError, match="Invalid encoded data"):
        shannon_fano_decode(codes, "10101010101")

def test_shannon_fano_different_inputs():
    """Test various input strings"""
    test_cases = [
        "ABCDEFG",
        "1234567890",
        "!@#$%^&*()",
        "Mixed Case String",
    ]
    
    for test_data in test_cases:
        codes = shannon_fano_encode(test_data)
        encoded = ''.join(codes[char] for char in test_data)
        decoded = shannon_fano_decode(codes, encoded)
        assert decoded == test_data