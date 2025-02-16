import pytest
from src.run_length_encoding import run_length_encode, run_length_decode

def test_run_length_encode_basic_string():
    """Test basic string encoding"""
    input_data = "AABBBCCCC"
    expected = [['A', 2], ['B', 3], ['C', 4]]
    assert run_length_encode(input_data) == expected

def test_run_length_encode_single_char():
    """Test encoding a single character"""
    input_data = "X"
    expected = [['X', 1]]
    assert run_length_encode(input_data) == expected

def test_run_length_encode_list():
    """Test encoding a list"""
    input_data = ['A', 'A', 'B', 'B', 'C']
    expected = [['A', 2], ['B', 2], ['C', 1]]
    assert run_length_encode(input_data) == expected

def test_run_length_decode_basic():
    """Test basic decoding"""
    input_data = [['A', 2], ['B', 3], ['C', 4]]
    expected = "AABBBCCCC"
    assert run_length_decode(input_data) == expected

def test_round_trip_encoding():
    """Test round trip encoding and decoding"""
    original = "AABBBCCCC"
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    assert decoded == original

def test_run_length_encode_error_handling():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        run_length_encode(123)
    
    with pytest.raises(ValueError):
        run_length_encode("")

def test_run_length_decode_error_handling():
    """Test error handling for invalid decode inputs"""
    with pytest.raises(TypeError):
        run_length_decode("not a list")
    
    with pytest.raises(ValueError):
        run_length_decode([])
    
    with pytest.raises(ValueError):
        run_length_decode([['A', -1]])
    
    with pytest.raises(ValueError):
        run_length_decode([['A', 'not a number']])