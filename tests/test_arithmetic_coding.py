import pytest
from src.arithmetic_coding import arithmetic_encode, arithmetic_decode

def test_arithmetic_encoding_basic():
    """Test basic arithmetic encoding and decoding"""
    message = "HELLO"
    compressed_value, prob_dist = arithmetic_encode(message)
    decoded_message = arithmetic_decode(compressed_value, prob_dist, len(message))
    assert decoded_message == message

def test_arithmetic_encoding_empty_string():
    """Test encoding and decoding an empty string"""
    message = ""
    compressed_value, prob_dist = arithmetic_encode(message)
    decoded_message = arithmetic_decode(compressed_value, prob_dist, len(message))
    assert decoded_message == message

def test_arithmetic_encoding_single_char():
    """Test encoding and decoding a single character"""
    message = "A"
    compressed_value, prob_dist = arithmetic_encode(message)
    decoded_message = arithmetic_decode(compressed_value, prob_dist, len(message))
    assert decoded_message == message

def test_arithmetic_encoding_repeated_chars():
    """Test encoding and decoding a string with repeated characters"""
    message = "AAAAA"
    compressed_value, prob_dist = arithmetic_encode(message)
    decoded_message = arithmetic_decode(compressed_value, prob_dist, len(message))
    assert decoded_message == message

def test_invalid_decode_inputs():
    """Test decoding with invalid inputs"""
    with pytest.raises(ValueError, match="Compressed value must be between 0 and 1"):
        arithmetic_decode(1.5, {"A": 1.0}, 1)
    
    with pytest.raises(ValueError, match="Probability distribution cannot be empty"):
        arithmetic_decode(0.5, {}, 1)

def test_arithmetic_encoding_complex_message():
    """Test encoding and decoding a more complex message"""
    message = "ABRACADABRA"
    compressed_value, prob_dist = arithmetic_encode(message)
    decoded_message = arithmetic_decode(compressed_value, prob_dist, len(message))
    assert decoded_message == message