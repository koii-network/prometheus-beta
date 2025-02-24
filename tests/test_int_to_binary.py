import pytest
from src.int_to_binary import int_to_binary

def test_zero_conversion():
    """Test conversion of zero to binary."""
    assert int_to_binary(0) == "0"

def test_positive_integers():
    """Test conversion of various positive integers to binary."""
    test_cases = [
        (1, "1"),
        (2, "10"),
        (3, "11"),
        (4, "100"),
        (10, "1010"),
        (15, "1111"),
        (16, "10000"),
        (255, "11111111")
    ]
    
    for num, expected in test_cases:
        assert int_to_binary(num) == expected

def test_large_number():
    """Test conversion of a large integer to binary."""
    large_num = 1024
    assert int_to_binary(large_num) == "10000000000"

def test_negative_input_raises_error():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        int_to_binary(-1)

def test_non_integer_input_raises_error():
    """Test that non-integer inputs raise a TypeError."""
    test_inputs = [
        3.14,
        "10",
        [1, 2, 3],
        None,
        True
    ]
    
    for invalid_input in test_inputs:
        with pytest.raises(TypeError, match="Input must be an integer"):
            int_to_binary(invalid_input)