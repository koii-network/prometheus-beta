import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from arithmetic_coding import arithmetic_encode, arithmetic_decode

def test_arithmetic_encoding_basic():
    """Test basic encoding with a simple message"""
    message = "HELLO"
    # Default probability model will be created automatically
    encoded = arithmetic_encode(message)
    assert isinstance(encoded, float)
    assert 0 <= encoded <= 1

def test_arithmetic_decoding_basic():
    """Test basic decoding of a simple message"""
    message = "HELLO"
    # Create a probability model
    prob_model = {
        'H': 0.2,
        'E': 0.2,
        'L': 0.3,
        'O': 0.3
    }
    
    # Encode the message
    encoded = arithmetic_encode(message, prob_model)
    
    # Decode the message
    decoded = arithmetic_decode(encoded, len(message), prob_model)
    
    assert decoded == message

def test_arithmetic_encoding_custom_prob_model():
    """Test encoding with a custom probability model"""
    message = "TEST"
    prob_model = {
        'T': 0.4,
        'E': 0.3,
        'S': 0.3
    }
    
    encoded = arithmetic_encode(message, prob_model)
    assert isinstance(encoded, float)
    assert 0 <= encoded <= 1

def test_empty_message_raises_error():
    """Test that empty message raises a ValueError"""
    with pytest.raises(ValueError, match="Message cannot be empty"):
        arithmetic_encode("")

def test_invalid_prob_model_raises_error():
    """Test that invalid probability model raises a ValueError"""
    message = "TEST"
    # Probability model that doesn't sum to 1
    prob_model = {
        'T': 0.5,
        'E': 0.6
    }
    
    with pytest.raises(ValueError, match="Invalid probability model"):
        arithmetic_encode(message, prob_model)

def test_round_trip_encoding_decoding():
    """Test full round-trip encoding and decoding"""
    message = "COMPRESS"
    prob_model = {
        'C': 0.2,
        'O': 0.1,
        'M': 0.1,
        'P': 0.1,
        'R': 0.1,
        'E': 0.2,
        'S': 0.1,
        'T': 0.1
    }
    
    # Encode
    encoded = arithmetic_encode(message, prob_model)
    
    # Decode
    decoded = arithmetic_decode(encoded, len(message), prob_model)
    
    assert decoded == message

def test_invalid_decode_value():
    """Test decoding with an invalid encoded value"""
    prob_model = {
        'A': 0.5,
        'B': 0.5
    }
    
    with pytest.raises(ValueError, match="Encoded value must be between 0 and 1"):
        arithmetic_decode(1.5, 3, prob_model)

def test_invalid_message_length():
    """Test decoding with an invalid message length"""
    prob_model = {
        'A': 0.5,
        'B': 0.5
    }
    
    with pytest.raises(ValueError, match="Message length must be positive"):
        arithmetic_decode(0.5, 0, prob_model)