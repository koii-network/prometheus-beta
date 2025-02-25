import pytest
import math
from src.arithmetic_coding import (
    arithmetic_encode, 
    arithmetic_decode, 
    calculate_probabilities, 
    validate_probability_model
)


def test_basic_encoding_decoding():
    """Test basic encoding and decoding of a simple string"""
    data = list("hello")
    prob_model = calculate_probabilities(data)
    
    # Encode
    encoded = arithmetic_encode(data, prob_model)
    
    # Decode
    decoded = arithmetic_decode(encoded, len(data), prob_model)
    
    assert decoded == data, "Decoding should recover original data"


def test_custom_probability_model():
    """Test encoding/decoding with a custom probability model"""
    custom_model = {
        'a': 0.3,
        'b': 0.5,
        'c': 0.2
    }
    data = ['a', 'b', 'c', 'a', 'b']
    
    # Encode
    encoded = arithmetic_encode(data, custom_model)
    
    # Decode
    decoded = arithmetic_decode(encoded, len(data), custom_model)
    
    assert decoded == data, "Decoding should work with custom probabilities"


def test_probability_model_validation():
    """Test validation of probability models"""
    # Valid model
    valid_model = {'a': 0.3, 'b': 0.7}
    validate_probability_model(valid_model)
    
    # Invalid models
    with pytest.raises(ValueError, match="Probabilities must sum to 1.0"):
        validate_probability_model({'a': 0.5, 'b': 0.6})
    
    with pytest.raises(ValueError, match="Probabilities must be between 0 and 1"):
        validate_probability_model({'a': 1.5, 'b': -0.5})
    
    with pytest.raises(ValueError, match="Probability model cannot be empty"):
        validate_probability_model({})


def test_edge_cases():
    """Test various edge cases"""
    # Empty input
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        arithmetic_encode([])
    
    # Single symbol
    single_symbol = ['x']
    prob_model = calculate_probabilities(single_symbol)
    encoded = arithmetic_encode(single_symbol, prob_model)
    decoded = arithmetic_decode(encoded, 1, prob_model)
    assert decoded == single_symbol, "Should handle single symbol correctly"


def test_string_input():
    """Test that the function works with string input"""
    data = "hello"
    prob_model = calculate_probabilities(list(data))
    
    # Encode
    encoded = arithmetic_encode(data, prob_model)
    
    # Decode
    decoded = arithmetic_decode(encoded, len(data), prob_model)
    
    assert decoded == list(data), "Should handle string input"


def test_precision_and_recovery():
    """Test encoding precision and data recovery"""
    data = ['a', 'b', 'c', 'a', 'b']
    prob_model = calculate_probabilities(data)
    
    # Encode
    encoded = arithmetic_encode(data, prob_model)
    
    # Decode multiple times with small variations
    for _ in range(10):
        # Simulate slight encoding variation
        variation = encoded * (1 + 1e-10)
        decoded = arithmetic_decode(variation, len(data), prob_model)
        
        assert decoded == data, f"Decoding failed with variation {variation}"


def test_invalid_decoding():
    """Test decoding with impossible scenarios"""
    prob_model = {'a': 0.5, 'b': 0.5}
    
    # Invalid data length
    with pytest.raises(ValueError, match="Data length must be positive"):
        arithmetic_decode(0.5, 0, prob_model)
    
    # Invalid encoded value out of bounds
    with pytest.raises(ValueError):
        arithmetic_decode(2.0, 5, prob_model)  # Out of [0, 1] range
    
    # Invalid probability model
    with pytest.raises(ValueError):
        arithmetic_decode(0.5, 5, {})