import pytest
from src.integer_to_binary import int_to_binary

def test_int_to_binary_zero():
    assert int_to_binary(0) == "0"

def test_int_to_binary_positive_numbers():
    assert int_to_binary(1) == "1"
    assert int_to_binary(2) == "10"
    assert int_to_binary(7) == "111"
    assert int_to_binary(10) == "1010"
    assert int_to_binary(15) == "1111"
    assert int_to_binary(256) == "100000000"

def test_int_to_binary_large_number():
    assert int_to_binary(1024) == "10000000000"

def test_int_to_binary_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_binary("10")
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_binary(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_binary(None)

def test_int_to_binary_negative_number():
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        int_to_binary(-5)