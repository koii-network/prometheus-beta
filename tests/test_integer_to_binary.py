import pytest
from src.integer_to_binary import int_to_binary

def test_zero_conversion():
    assert int_to_binary(0) == "0"

def test_positive_integers():
    test_cases = [
        (1, "1"),
        (2, "10"),
        (3, "11"),
        (4, "100"),
        (5, "101"),
        (10, "1010"),
        (15, "1111"),
        (16, "10000"),
        (255, "11111111")
    ]
    
    for number, expected in test_cases:
        assert int_to_binary(number) == expected

def test_type_error():
    with pytest.raises(TypeError, match="Input must be an integer"):
        int_to_binary("not an integer")
        int_to_binary(3.14)
        int_to_binary([1, 2, 3])

def test_negative_input():
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        int_to_binary(-1)
        int_to_binary(-10)