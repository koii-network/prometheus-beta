import pytest
from src.integer_to_binary import convert_to_binary

def test_convert_to_binary_zero():
    assert convert_to_binary(0) == "0"

def test_convert_to_binary_positive_numbers():
    assert convert_to_binary(1) == "1"
    assert convert_to_binary(2) == "10"
    assert convert_to_binary(5) == "101"
    assert convert_to_binary(10) == "1010"
    assert convert_to_binary(255) == "11111111"

def test_convert_to_binary_large_number():
    assert convert_to_binary(1024) == "10000000000"

def test_convert_to_binary_invalid_input_types():
    with pytest.raises(TypeError):
        convert_to_binary("10")
    with pytest.raises(TypeError):
        convert_to_binary(3.14)
    with pytest.raises(TypeError):
        convert_to_binary(None)

def test_convert_to_binary_negative_number():
    with pytest.raises(ValueError):
        convert_to_binary(-5)