import pytest
import math
from src.arithmetic_coding import arithmetic_encode, arithmetic_decode

def test_arithmetic_encode_basic():
    # Test encoding with simple input and uniform probabilities
    data = ['A', 'B', 'C']
    prob_model = {'A': 1/3, 'B': 1/3, 'C': 1/3}
    encoded = arithmetic_encode(data, prob_model)
    assert 0 <= encoded <= 1, "Encoded value should be between 0 and 1"

def test_arithmetic_decode_basic():
    # Test decoding with simple input
    data = ['A', 'B', 'C']
    prob_model = {'A': 1/3, 'B': 1/3, 'C': 1/3}
    encoded = arithmetic_encode(data, prob_model)
    decoded = arithmetic_decode(encoded, len(data), prob_model)
    assert decoded == data, "Decoded data should match original input"

def test_arithmetic_encode_string_input():
    # Test encoding with string input
    data = "HELLO"
    encoded = arithmetic_encode(data)
    assert 0 <= encoded <= 1, "Encoded value should be between 0 and 1"

def test_arithmetic_round_trip():
    # Test complete encode-decode round trip
    data = ['A', 'B', 'A', 'C', 'B']
    prob_model = {'A': 0.4, 'B': 0.3, 'C': 0.3}
    encoded = arithmetic_encode(data, prob_model)
    decoded = arithmetic_decode(encoded, len(data), prob_model)
    assert decoded == data, "Round trip encoding and decoding should preserve data"

def test_empty_input_raises_error():
    # Test that empty input raises a ValueError
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        arithmetic_encode([])

def test_invalid_probability_model_sum():
    # Test that an invalid probability model raises an error
    data = ['A', 'B']
    prob_model = {'A': 0.5, 'B': 0.6}  # Probabilities sum > 1
    with pytest.raises(ValueError, match=r"Probabilities must sum to 1\.0 \(current sum: \d+\.\d+\)"):
        arithmetic_encode(data, prob_model)

def test_missing_symbol_in_probability_model():
    # Test that a missing symbol in probability model raises an error
    data = ['A', 'B', 'C']
    prob_model = {'A': 0.3, 'B': 0.7}  # Missing probability for 'C'
    with pytest.raises(ValueError, match="Missing probability for symbols"):
        arithmetic_encode(data, prob_model)

def test_decode_with_invalid_length():
    # Test decoding with invalid data length
    prob_model = {'A': 1/3, 'B': 1/3, 'C': 1/3}
    encoded = 0.5
    with pytest.raises(ValueError, match="Data length must be positive"):
        arithmetic_decode(encoded, 0, prob_model)

def test_different_probability_distributions():
    # Test encoding and decoding with different probability distributions
    test_cases = [
        (['A', 'A', 'B', 'B'], {'A': 0.6, 'B': 0.4}),
        (['X', 'Y', 'Z'], {'X': 0.2, 'Y': 0.3, 'Z': 0.5}),
    ]
    
    for data, prob_model in test_cases:
        encoded = arithmetic_encode(data, prob_model)
        decoded = arithmetic_decode(encoded, len(data), prob_model)
        assert decoded == data, f"Failed for data {data} with {prob_model}"