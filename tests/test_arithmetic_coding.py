import pytest
from src.arithmetic_coding import arithmetic_encode, arithmetic_decode

def test_arithmetic_coding_basic():
    # Test basic encoding and decoding
    original = "hello"
    
    # Calculate frequencies for decoding
    freq = {}
    for char in original:
        freq[char] = freq.get(char, 0) + 1
    
    # Encode
    compressed = arithmetic_encode(original)
    
    # Decode
    decoded = arithmetic_decode(compressed, len(original), freq)
    
    assert decoded == original

def test_empty_string():
    # Test empty string
    assert arithmetic_encode("") == 0.0

def test_single_character():
    # Test single character string
    original = "a"
    freq = {"a": 1}
    
    compressed = arithmetic_encode(original)
    decoded = arithmetic_decode(compressed, len(original), freq)
    
    assert decoded == original

def test_repeated_characters():
    # Test string with repeated characters
    original = "aaaa"
    
    freq = {"a": 4}
    
    compressed = arithmetic_encode(original)
    decoded = arithmetic_decode(compressed, len(original), freq)
    
    assert decoded == original

def test_complex_string():
    # Test more complex string
    original = "abracadabra"
    
    # Calculate frequencies for decoding
    freq = {}
    for char in original:
        freq[char] = freq.get(char, 0) + 1
    
    compressed = arithmetic_encode(original)
    decoded = arithmetic_decode(compressed, len(original), freq)
    
    assert decoded == original