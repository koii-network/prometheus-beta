import pytest
from src.int_to_binary import int_to_binary

def test_int_to_binary_zero():
    assert int_to_binary(0) == "0"

def test_int_to_binary_positive_numbers():
    assert int_to_binary(1) == "1"
    assert int_to_binary(2) == "10"
    assert int_to_binary(5) == "101"
    assert int_to_binary(10) == "1010"
    assert int_to_binary(42) == "101010"

def test_int_to_binary_large_number():
    assert int_to_binary(255) == "11111111"
    assert int_to_binary(1024) == "10000000000"

def test_int_to_binary_invalid_input():
    # Test TypeError for non-integer inputs
    with pytest.raises(TypeError):
        int_to_binary("not an int")
    with pytest.raises(TypeError):
        int_to_binary(3.14)
    with pytest.raises(TypeError):
        int_to_binary(None)

def test_int_to_binary_negative_input():
    # Test ValueError for negative numbers
    with pytest.raises(ValueError):
        int_to_binary(-1)