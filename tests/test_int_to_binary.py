import pytest
from src.int_to_binary import int_to_binary

def test_positive_integers():
    assert int_to_binary(0) == "0"
    assert int_to_binary(1) == "1"
    assert int_to_binary(2) == "10"
    assert int_to_binary(7) == "111"
    assert int_to_binary(10) == "1010"
    assert int_to_binary(16) == "10000"

def test_large_number():
    assert int_to_binary(255) == "11111111"
    assert int_to_binary(1024) == "10000000000"

def test_invalid_input():
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        int_to_binary(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_binary(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_binary("not a number")