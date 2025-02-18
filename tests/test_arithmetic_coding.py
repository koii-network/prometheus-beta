import pytest
from src.arithmetic_coding import arithmetic_encode, arithmetic_decode

def test_arithmetic_encoding_basic():
    # Test basic encoding
    data = "hello"
    encoded = arithmetic_encode(data)
    assert isinstance(encoded, float)
    assert 0 <= encoded <= 1

def test_arithmetic_encoding_empty_string():
    # Test encoding of empty string
    data = ""
    encoded = arithmetic_encode(data)
    assert encoded == 0.5

def test_arithmetic_encoding_decoding_simple():
    # Test full encode-decode cycle
    data = "hello"
    
    # Calculate character frequencies
    char_freq = {}
    for char in data:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Encode
    encoded = arithmetic_encode(data)
    
    # Decode
    decoded = arithmetic_decode(encoded, len(data), char_freq)
    
    assert decoded == data

def test_arithmetic_encoding_decoding_complex():
    # Test with a more complex string
    data = "programming"
    
    # Calculate character frequencies
    char_freq = {}
    for char in data:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    # Encode
    encoded = arithmetic_encode(data)
    
    # Decode
    decoded = arithmetic_decode(encoded, len(data), char_freq)
    
    assert decoded == data

def test_arithmetic_decode_invalid_inputs():
    # Test error handling
    with pytest.raises(ValueError):
        arithmetic_decode("not a number", 5, {"a": 1, "b": 2})
    
    with pytest.raises(ValueError):
        arithmetic_decode(1.5, 5, {"a": 1, "b": 2})

def test_arithmetic_encode_different_strings():
    # Ensure different strings produce different encodings
    data1 = "hello"
    data2 = "world"
    
    encoded1 = arithmetic_encode(data1)
    encoded2 = arithmetic_encode(data2)
    
    assert encoded1 != encoded2