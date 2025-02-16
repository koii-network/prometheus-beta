import pytest
from src.arithmetic_coding import arithmetic_encode, arithmetic_decode

def test_arithmetic_coding_string():
    # Test with a string input
    input_data = "HELLO"
    encoded = arithmetic_encode(input_data)
    
    # Check returned dictionary has correct keys
    assert 'probabilities' in encoded
    assert 'compressed_value' in encoded
    
    # Check probabilities
    assert all(0 <= prob <= 1 for prob in encoded['probabilities'].values())
    assert abs(sum(encoded['probabilities'].values()) - 1.0) < 1e-10
    
    # Verify decode
    decoded = arithmetic_decode(encoded, len(input_data))
    assert len(decoded) == len(input_data)
    
    # Test different input types (string and list)
    list_input = list(input_data)
    list_encoded = arithmetic_encode(list_input)
    assert list_encoded == encoded

def test_arithmetic_coding_list():
    # Test with a list input
    input_data = ['A', 'B', 'C', 'A', 'B', 'A']
    encoded = arithmetic_encode(input_data)
    
    # Check returned dictionary has correct keys
    assert 'probabilities' in encoded
    assert 'compressed_value' in encoded
    
    # Check probabilities
    assert all(0 <= prob <= 1 for prob in encoded['probabilities'].values())
    assert abs(sum(encoded['probabilities'].values()) - 1.0) < 1e-10
    
    # Verify decode
    decoded = arithmetic_decode(encoded, len(input_data))
    assert len(decoded) == len(input_data)

def test_arithmetic_coding_edge_cases():
    # Test with single character
    single_char = "A"
    encoded = arithmetic_encode(single_char)
    decoded = arithmetic_decode(encoded, len(single_char))
    assert decoded == list(single_char)
    
    # Test with empty input
    with pytest.raises(ZeroDivisionError):
        arithmetic_encode([])

def test_arithmetic_coding_probabilistic():
    # Test with more complex input
    input_data = "AAABBBCCCDDD"
    encoded = arithmetic_encode(input_data)
    decoded = arithmetic_decode(encoded, len(input_data))
    
    # Check frequency preservation
    input_freq = {char: input_data.count(char) for char in set(input_data)}
    decoded_freq = {char: decoded.count(char) for char in set(decoded)}
    
    assert input_freq == decoded_freq